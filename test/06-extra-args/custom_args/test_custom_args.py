import pytest

def test_requires_cmdopt(request):
    """Fails unless '--cmdopt=<value>' is passed to pytest."""
    if request.config.getoption("--cmdopt") is None:
        pytest.fail("Test requires '--cmdopt' to properly execute the test.")
    assert True
