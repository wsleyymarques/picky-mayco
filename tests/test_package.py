from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "consume",
    "picky-mayco",
    "picky-mayco-backend",
    "picky-mayco-docs",
    "picky-mayco-frontend",
    "picky-mayco-images",
    "picky-mayco-qa",
}


class PackageTests(unittest.TestCase):
    def run_script(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *arguments],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_validation_passes(self) -> None:
        result = self.run_script("scripts/validate.py")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_installer_copies_every_skill_and_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory(prefix="picky-mayco-test-") as temporary:
            destination = Path(temporary) / "skills"
            first = self.run_script("scripts/install.py", "--dest", str(destination))
            self.assertEqual(first.returncode, 0, first.stderr)
            installed = {path.name for path in destination.iterdir() if path.is_dir()}
            self.assertEqual(installed, EXPECTED_SKILLS)

            second = self.run_script("scripts/install.py", "--dest", str(destination))
            self.assertEqual(second.returncode, 3)
            self.assertIn("Installation stopped", second.stderr)


if __name__ == "__main__":
    unittest.main()
