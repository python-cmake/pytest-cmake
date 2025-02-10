cmake_minimum_required(VERSION 3.20)

project(TestExtraArgs)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestExtraArgs.extraArgs
    EXTRA_ARGS "--capture=no" "--cmdopt=demo"
    DEPENDS test_extra_args.py
)

set(EXPECTED
    "TestExtraArgs.extraArgs.test_requires_no_capture"
    "TestExtraArgs.extraArgs.test_requires_args"
)

add_test(
    NAME TestExtraArgs.Validate
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestExtraArgs.extraArgs"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_SOURCE_DIR}/../01-modify-name/compare_discovered_tests.cmake
)

# Negative Test which suppresses test discovery
pytest_discover_tests(
    TestDiscoveryArgsSupressDiscovery
    DISCOVERY_EXTRA_ARGS "-v"
    DEPENDS test_extra_args.py
)

# Test which re-enables test discovery due to usage of "-v" command line flag
# during test discovery
pytest_discover_tests(
    TestDiscoveryArgsDiscovery
    EXTRA_ARGS "--capture=no" "--cmdopt=discover"
    DISCOVERY_EXTRA_ARGS "-v" "-q"
    INCLUDE_FILE_PATH
    DEPENDS test_extra_args.py
)

set(EXPECTED
    "TestDiscoveryArgsDiscovery.test_extra_args.test_requires_no_capture"
    "TestDiscoveryArgsDiscovery.test_extra_args.test_requires_args"
)

add_test(
    NAME TestDiscoveryArgsDiscovery.Validate
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestDiscoveryArgsDiscovery.test_extra_args"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_SOURCE_DIR}/../01-modify-name/compare_discovered_tests.cmake
)
