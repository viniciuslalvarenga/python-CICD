"""
Test Project Generation
"""

import shutil
from pathlib import Path
from typing import Generator

import pytest

from tests.utils.project import generate_project


@pytest.fixture(scope="function")
def project_dir() -> Generator[Path, None, None]:
    template_values = {
        "repo_name": "test_repo",
    }
    generated_proj_dir: Path = generate_project(template_value=template_values)
    yield generated_proj_dir
    shutil.rmtree(path=generated_proj_dir)


def test_can_generate_project(project_dir: Path):
    """Test that project can be generated."""
    assert project_dir.exists()
