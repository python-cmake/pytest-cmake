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

# add_test(NAME TestPytestArgs.Validate.test_no_discovered_w_args_v_s
#     COMMAND ${CMAKE_COMMAND}
#     -D "TEST_PREFIX=\"\""
#     -D "EXPECTED=\"\""
#     -P ${CMAKE_CURRENT_SOURCE_DIR}/../01-modify-name/compare_discovered_tests.cmake
# )

pytest_discover_tests(
	pytestargs_basic_args
	PYTEST_ARGS -v -s -q
	DEPENDS test_basic.py
)

add_test(NAME TestPytestArgs.Validate.test_basic
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=pytestargs_basic_args.test_basic"
    -D "EXPECTED=pytestargs_basic_args.test_basic"
    -P ${CMAKE_CURRENT_SOURCE_DIR}/../01-modify-name/compare_discovered_tests.cmake
)

# Currently quoted args are not supported
pytest_discover_tests(
	pytestargs_basic_args_quoted
	PYTEST_ARGS "-v -s -q"
	DEPENDS test_basic.py
)

# semi-colon value to the PYTEST_ARGS is considered as a list
pytest_discover_tests(
	pytestargs_basic_args_semicolon
	PYTEST_ARGS -v;-s;-q
	DEPENDS test_basic.py
)

add_test(NAME TestPytestArgsSemicolon.Validate.test_basic
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=pytestargs_basic_args_semicolon.test_basic"
    -D "EXPECTED=pytestargs_basic_args_semicolon.test_basic"
    -P ${CMAKE_CURRENT_SOURCE_DIR}/../01-modify-name/compare_discovered_tests.cmake
)
