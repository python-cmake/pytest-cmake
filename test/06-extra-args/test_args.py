import pytest

def test_requires_no_capture(request):
    """Fails unless '--capture=no' is passed to pytest."""
    if "--capture=no" not in request.config.invocation_params.args:
        pytest.fail("Test requires '--capture=no' to properly display output.")
    assert True
