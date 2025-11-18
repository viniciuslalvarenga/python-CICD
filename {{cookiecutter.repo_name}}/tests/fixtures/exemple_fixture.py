"""Fixture to generate a project directory for testing."""

# from pathlib import Path bla
from uuid import uuid4

import pytest

# THIS_DIR = Path(__file__).parent bla
from tests.consts import PROJECT_DIR

# PROJECT_DIR = (THIS_DIR / "../../").resolve() bla


@pytest.fixture(scope="session")
def generate_test_session_id() -> str:
    """Generate a unique test session ID."""
    return str(PROJECT_DIR.name) + str(uuid4())[:6]
