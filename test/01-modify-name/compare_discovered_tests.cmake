cmake_minimum_required(VERSION 3.20)

execute_process(
    COMMAND ${CMAKE_CTEST_COMMAND} --show-only
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    OUTPUT_VARIABLE test_output
)

string(REGEX MATCHALL "${TEST_PREFIX}[^\n]*" discovered_tests "${test_output}")

if (NOT discovered_tests)
    message(FATAL_ERROR "'${TEST_PREFIX}': No tests discovered.")
endif()

list(SORT discovered_tests)
list(SORT EXPECTED)

string(JOIN ";" discovered_tests_string ${discovered_tests})
string(JOIN ";" expected_tests_string ${EXPECTED})

if(NOT "${discovered_tests_string}" STREQUAL "${expected_tests_string}")
    message(FATAL_ERROR
        "'${TEST_PREFIX}': The discovered tests list does not match the expected list.\n"
        "Expected: ${expected_tests_string}\n"
        "Found: ${discovered_tests_string}"
    )
endif()
