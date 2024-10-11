import os
import pytest

def test_env():
    """Ensure that the environment variables have been set."""
    assert os.environ.get("ENV_VAR1", "") == "VALUE1"
    assert os.environ.get("ENV_VAR2", "") == "VALUE2"
    assert os.environ.get("ENV_VAR3", "") == "PATH1:PATH2:PATH3"
