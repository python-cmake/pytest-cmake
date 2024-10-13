cmake_minimum_required(VERSION 3.20)

project(TestProperties)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestProperties.Timeout
    PROPERTIES
        TIMEOUT 120
)
add_test(NAME TestProperties.Validate.Timeout
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestProperties.Timeout"
    -D "TEST_PROPERTY=TIMEOUT"
    -D "EXPECTED_VALUE=120.0"
    -P ${CMAKE_CURRENT_LIST_DIR}/check_test_property.cmake
)

pytest_discover_tests(
    TestProperties.Labels
    PROPERTIES
        LABELS "foo\;bar"
)
add_test(NAME TestProperties.Validate.Labels
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestProperties.Labels"
    -D "TEST_PROPERTY=LABELS"
    -D "EXPECTED_VALUE=[ \"bar\", \"foo\" ]"
    -P ${CMAKE_CURRENT_LIST_DIR}/check_test_property.cmake
)

pytest_discover_tests(
    TestProperties.Disabled
    PROPERTIES
        DISABLED ON
)
add_test(NAME TestProperties.Validate.Disabled
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestProperties.Disabled"
    -D "TEST_PROPERTY=DISABLED"
    -D "EXPECTED_VALUE=ON"
    -P ${CMAKE_CURRENT_LIST_DIR}/check_test_property.cmake
)

pytest_discover_tests(
    TestProperties.SkipReturnCode
    PROPERTIES
        SKIP_RETURN_CODE 77
)
add_test(NAME TestProperties.Validate.SkipReturnCode
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestProperties.SkipReturnCode"
    -D "TEST_PROPERTY=SKIP_RETURN_CODE"
    -D "EXPECTED_VALUE=77"
    -P ${CMAKE_CURRENT_LIST_DIR}/check_test_property.cmake
)
