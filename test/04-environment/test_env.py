import os
import platform

def test_env():
    """Ensure that the environment variables have been set."""
    assert os.environ.get("KEY1", "") == "VALUE1"
    assert os.environ.get("KEY2", "") == "VALUE2"
    assert os.environ.get("KEY3", "") == "PATH1:PATH2:PATH3"

    if platform.system() == "Windows":
        assert os.environ.get("KEY4", "") == "PATH1;PATH2;PATH3"
        assert os.environ.get("KEY5", "") == r"C:\Path\To\Dir1;C:\Path\To\Dir2"
    else:
        assert os.environ.get("KEY4", "") == "PATH1\;PATH2\;PATH3"
        assert os.environ.get("KEY5", "") == r"C:\Path\To\Dir1\;C:\Path\To\Dir2"

    assert os.environ.get("K3Y4", "") == "SPECIAL$VALUE!@#%^&*"
