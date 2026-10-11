#!/usr/bin/env python3
"""Validate the Picky Mayco plugin and its packaged skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
REQUIRED_SKILLS = {
    "consume",
    "picky-mayco",
    "picky-mayco-backend",
    "picky-mayco-docs",
    "picky-mayco-frontend",
    "picky-mayco-images",
    "picky-mayco-qa",
}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
LOCAL_PATH_PATTERN = re.compile(r"/(?:Users|home)/[^\s/]+/")
UNFINISHED_PATTERN = re.compile(
    r"\b(?:" + "|".join(("TO" + "DO", "FIX" + "ME", "CHANGE" + "ME")) + r")\b"
)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")

    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as error:
        raise ValueError("missing closing frontmatter delimiter") from error

    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.+?)\s*$", line)
        if not match:
            continue
        key, value = match.groups()
        values[key] = value.strip("\"'")
    return values


def validate_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    prose = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for target in MARKDOWN_LINK_PATTERN.findall(prose):
        clean_target = target.split("#", 1)[0]
        if not clean_target or clean_target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (path.parent / clean_target).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link {target!r}")


def validate() -> list[str]:
    errors: list[str] = []

    manifest_path = ROOT / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"plugin.json: {error}"]

    for field in ("$schema", "name", "version", "description", "license"):
        if not manifest.get(field):
            errors.append(f"plugin.json: missing {field}")
    if manifest.get("name") != "picky-mayco":
        errors.append("plugin.json: name must be picky-mayco")

    discovered = {
        child.name
        for child in SKILLS_ROOT.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    }
    missing = REQUIRED_SKILLS - discovered
    if missing:
        errors.append(f"skills: missing required skills: {', '.join(sorted(missing))}")

    for skill_name in sorted(discovered):
        skill_dir = SKILLS_ROOT / skill_name
        skill_file = skill_dir / "SKILL.md"
        try:
            frontmatter = parse_frontmatter(skill_file)
        except ValueError as error:
            errors.append(f"{skill_file.relative_to(ROOT)}: {error}")
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if name != skill_name:
            errors.append(f"{skill_file.relative_to(ROOT)}: name {name!r} does not match directory")
        if len(name) > 64 or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{skill_file.relative_to(ROOT)}: invalid skill name {name!r}")
        if not description:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")

        metadata = skill_dir / "agents" / "openai.yaml"
        if not metadata.is_file():
            errors.append(f"{metadata.relative_to(ROOT)}: missing Codex metadata")
        else:
            metadata_text = metadata.read_text(encoding="utf-8")
            for field in ("display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation:"):
                if field not in metadata_text:
                    errors.append(f"{metadata.relative_to(ROOT)}: missing {field}")

    for markdown_file in ROOT.rglob("*.md"):
        if ".git" not in markdown_file.parts:
            validate_links(markdown_file, errors)

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if LOCAL_PATH_PATTERN.search(text):
            errors.append(f"{relative}: contains an absolute user path")
        if UNFINISHED_PATTERN.search(text):
            errors.append(f"{relative}: contains unfinished marker")
        if "-----BEGIN " + "PRIVATE KEY-----" in text:
            errors.append(f"{relative}: contains private key material")

    router = (SKILLS_ROOT / "picky-mayco" / "SKILL.md").read_text(encoding="utf-8")
    for dependency in REQUIRED_SKILLS - {"picky-mayco"}:
        if f"${dependency}" not in router:
            errors.append(f"skills/picky-mayco/SKILL.md: missing dependency ${dependency}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated plugin and {len(REQUIRED_SKILLS)} required skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
