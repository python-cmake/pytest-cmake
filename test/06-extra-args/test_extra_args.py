import pytest

def test_requires_no_capture(request):
    """Fails unless '--capture=no' is passed to pytest."""
    if "--capture=no" not in request.config.invocation_params.args:
        pytest.fail("Test requires '--capture=no' to properly display output.")
    assert True


def test_requires_args(cmdopt):
    """Fails unless '--cmdopt=<value>' is passed to pytest."""
    if cmdopt != None:
        print(f"Option Value: cmdopt: {cmdopt}")
    else:
        pytest.fail("Test requires '--cmdopt=<value>' to properly execute the test.")
    pass
