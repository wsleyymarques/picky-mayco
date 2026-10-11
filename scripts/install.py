#!/usr/bin/env python3
"""Install packaged Picky Mayco skills into a local Agent Skills directory."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"


def default_destination() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def available_skills() -> dict[str, Path]:
    return {
        path.name: path
        for path in sorted(SKILLS_ROOT.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=default_destination(),
        help="skills directory; defaults to CODEX_HOME/skills or ~/.codex/skills",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="skills",
        help="install one named skill; repeat to select multiple; default installs all",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skills = available_skills()
    selected = args.skills or list(skills)
    unknown = sorted(set(selected) - set(skills))
    if unknown:
        print(f"Unknown skills: {', '.join(unknown)}", file=sys.stderr)
        return 2

    validation = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate.py")],
        cwd=ROOT,
        check=False,
    )
    if validation.returncode:
        return validation.returncode

    destination = args.dest.expanduser().resolve()
    conflicts = [name for name in selected if (destination / name).exists()]
    if conflicts:
        print(
            "Installation stopped; destination already contains: " + ", ".join(conflicts),
            file=sys.stderr,
        )
        return 3

    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="picky-mayco-install-") as temporary:
        staging = Path(temporary)
        for name in selected:
            shutil.copytree(skills[name], staging / name)
        for name in selected:
            shutil.move(str(staging / name), destination / name)

    print(f"Installed {len(selected)} skills into {destination}")
    print("Skills become available on the next agent turn.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
