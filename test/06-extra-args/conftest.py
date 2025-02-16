def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", help="custom options"
    )
