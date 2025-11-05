"""
Test Project Generation
"""

import json
import subprocess
from pathlib import Path

THIS_DIR = Path(__file__).parent
PROJECT_DIR = THIS_DIR / "../"


def test_can_generate_project():
    """
    execute: cookiecutter <template directory> ...
    """
    cookiecutter_config = {"default_context": {"repo_name": "test_repo"}}

    cookiecutter_config_fpath = PROJECT_DIR / "cookiecutter_test_config.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
        "--verbose",
    ]

    subprocess.run(cmd, check=True)
    generated_proj_dir = PROJECT_DIR / "sample" / cookiecutter_config["default_context"]["repo_name"]
    assert generated_proj_dir.exists()
