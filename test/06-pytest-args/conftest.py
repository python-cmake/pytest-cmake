import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", help="custom options"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")