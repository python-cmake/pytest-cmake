cmake_minimum_required(VERSION 3.20)

project(TestPytestArgs)

find_package(Pytest REQUIRED)

enable_testing()

# The --help flag will suppress test discovery
pytest_discover_tests(
	pytestargs_no_test_discovered_w_help
	PYTEST_ARGS --help
	DEPENDS test_basic.py
)

# The -v flag will suppress test discovery
# as the output for the command: pytest --co -q
# Is affected by this commandline flag
pytest_discover_tests(
	pytestargs_no_test_discovered_w_args_v
	PYTEST_ARGS -v
	DEPENDS test_basic.py
)

pytest_discover_tests(
	pytestargs_no_test_discovered_w_args_v_s
	PYTEST_ARGS -v -s
	DEPENDS test_basic.py
)

pytest_discover_tests(
	pytestargs_basic_args
	PYTEST_ARGS -v -s -q
	DEPENDS test_basic.py
)

# Currently quoted args are not supported
# pytest_discover_tests(
# 	pytestargs_basic_args_quoted
# 	PYTEST_ARGS "-v -s -q"
# 	DEPENDS test_basic.py
# )

