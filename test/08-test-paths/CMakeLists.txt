cmake_minimum_required(VERSION 3.20)

project(TestCustomPaths)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestCustomPaths.FromConfig
)
set(EXPECTED
    "TestCustomPaths.FromConfig.test_addition"
    "TestCustomPaths.FromConfig.test_concat"
    "TestCustomPaths.FromConfig.test_power"
    "TestCustomPaths.FromConfig.test_substraction"
    "TestCustomPaths.FromConfig.test_upper"
)
add_test(NAME TestCustomPaths.Validate.FromConfig
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestCustomPaths.FromConfig"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/../utils/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestCustomPaths.BundledFromConfig
    BUNDLE_TESTS
)
set(EXPECTED
    "TestCustomPaths.BundledFromConfig"
)
add_test(NAME TestCustomPaths.Validate.BundledFromConfig
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestCustomPaths.BundledFromConfig"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/../utils/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestCustomPaths.FilePaths
    TEST_PATHS
        ${CMAKE_CURRENT_LIST_DIR}/test_a/math/test_add.py
        test_a/choice.py
        test_b/test_concat.py
)
set(EXPECTED
    "TestCustomPaths.FilePaths.test_addition"
    "TestCustomPaths.FilePaths.test_concat"
    "TestCustomPaths.FilePaths.test_random"
)
add_test(NAME TestCustomPaths.Validate.FilePaths
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestCustomPaths.FilePaths"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/../utils/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestCustomPaths.DirPaths
    TEST_PATHS
        test_a
        ${CMAKE_CURRENT_LIST_DIR}/test_b/math
)
set(EXPECTED
    "TestCustomPaths.DirPaths.test_addition"
    "TestCustomPaths.DirPaths.test_power"
    "TestCustomPaths.DirPaths.test_substraction"
    "TestCustomPaths.DirPaths.test_upper"
)
add_test(NAME TestCustomPaths.Validate.DirPaths
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestCustomPaths.DirPaths"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/../utils/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestCustomPaths.WithWorkingDirectory
    TEST_PATHS
        math
        choice.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test_a
)
set(EXPECTED
    "TestCustomPaths.WithWorkingDirectory.test_addition"
    "TestCustomPaths.WithWorkingDirectory.test_random"
)
add_test(NAME TestCustomPaths.Validate.WithWorkingDirectory
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestCustomPaths.WithWorkingDirectory"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/../utils/compare_discovered_tests.cmake
)
