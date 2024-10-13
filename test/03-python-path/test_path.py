import os

PREPENDED_PATH = "@EXPECTED@"

def test_path():
    """Ensure that the path has been prepended as expected."""
    current_path = os.environ.get("PYTHONPATH", "")

    assert current_path == PREPENDED_PATH or current_path.startswith(PREPENDED_PATH + os.pathsep), \
        f"PYTHONPATH does not start with {PREPENDED_PATH}, found: {current_path}"
