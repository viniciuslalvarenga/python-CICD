"""
Fixture to generate a project directory for testing.
"""

from uuid import uuid4

import pytest

from tests.const import PROJECT_DIR


@pytest.fixture(scope="session")
def generate_test_session_id() -> str:
    return str(PROJECT_DIR.name) + str(uuid4())[:6]
