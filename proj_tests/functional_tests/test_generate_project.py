"""Test Project Generation Functionality."""

from pathlib import Path


def test_can_generate_project(project_dir: Path):
    """Test that project can be generated."""
    assert project_dir.exists()
