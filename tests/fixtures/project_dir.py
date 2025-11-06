""" """

import shutil
import subprocess
from pathlib import Path
from typing import Generator

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="function")
def project_dir() -> Generator[Path, None, None]:
    template_values = {
        "repo_name": "test_repo",
    }
    generated_proj_dir: Path = generate_project(template_value=template_values)
    initialize_git_repo(generated_proj_dir)
    # Run linting to fix any formatting issues in the generated project antes dos testes com o mesmo commando
    subprocess.run(["make", "lint-ci"], cwd=generated_proj_dir, check=False)
    yield generated_proj_dir
    shutil.rmtree(path=generated_proj_dir)
