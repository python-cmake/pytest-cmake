cmake_minimum_required(VERSION 3.20)

project(TestPytestArgs)

find_package(Pytest REQUIRED)

enable_testing()

# The --help flag will supress test discovery
pytest_discover_tests(
	pytestargs.basic
	PYTEST_ARGS --help
	DEPENDS test_basic.py
)

