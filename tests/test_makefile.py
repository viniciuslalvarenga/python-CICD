"""
Setup
    1. Generate project using cookiecutter
    2. Create a virtual environment and install project dependencies(to all tests, could separete it)

Tests:
    3. Run tests
    4. Run linting

Cleanup/Teardown:
    5. Remove virtual environment
    6. Remove generated project
"""

import subprocess
from pathlib import Path


def test_linting_passes(project_dir: Path):
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test_tests_pass():
    pass


def test_install_succeeds():
    pass
