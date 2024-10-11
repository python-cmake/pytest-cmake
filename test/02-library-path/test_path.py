import os
import platform
import pytest

PREPENDED_PATH = "@EXPECTED@"

def test_path():
    """Ensure that the path has been prepended as expected."""
    env_vars = {
        "Linux": "LD_LIBRARY_PATH",
        "Darwin": "DYLD_LIBRARY_PATH",
    }
    env_var = env_vars.get(platform.system(), "PATH")
    current_path = os.environ.get(env_var, "")

    assert current_path == PREPENDED_PATH or current_path.startswith(PREPENDED_PATH + os.pathsep), \
        f"{env_var} does not start with {PREPENDED_PATH}, found: {current_path}"
