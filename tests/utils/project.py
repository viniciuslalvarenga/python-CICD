"""
Helper functions for project generation tests.
"""

import json
import subprocess
from copy import deepcopy
from typing import Dict

## Import project directory constant(funciona mesmo nao sendo full qualified page- video 159)
from tests.const import PROJECT_DIR


def generate_project(template_value: Dict[str, str]):
    """
    execute: cookiecutter <template directory> ...
    """
    # NOTE: dicionary is modified by cookiecutter, so we deepcopy it(arg is pointer)
    template_values: Dict[str, str] = deepcopy(template_value)

    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / "tests/cookiecutter_test_config.json"
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
    generated_proj_dir = PROJECT_DIR / "sample" / template_values["repo_name"]
    return generated_proj_dir
