cmake_minimum_required(VERSION 3.20)

execute_process(
    COMMAND ${CMAKE_CTEST_COMMAND}
        --show-only=json-v1
        -R "${TEST_PREFIX}"
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    OUTPUT_VARIABLE test_output
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Trailing slashes in Windows environment paths produce '\;', leading to JSON
# parsing issues. Replace '\;' with ';' to resolve.
string(REPLACE [[\;]] [[;]] test_output "${test_output}")

string(JSON num_tests LENGTH ${test_output} tests)

if (num_tests EQUAL 0)
    message(FATAL_ERROR "'${TEST_PREFIX}': No tests discovered.")
endif()

string(JSON tests_array GET ${test_output} tests)
math(EXPR last_test_index "${num_tests}-1")

foreach (i RANGE 0 ${last_test_index})
    string(JSON test_name GET ${tests_array} ${i} name)
    string(JSON num_properties LENGTH ${tests_array} ${i} properties)

    if (num_properties EQUAL 0)
        message(FATAL_ERROR "Test '${test_name}' does not have properties.")
    endif()

    string(JSON properties GET ${tests_array} ${i} properties)
    math(EXPR last_property_index "${num_properties}-1")

    set(property_found 0)

    foreach (j RANGE 0 ${last_property_index})
        string(JSON property_name GET ${properties} ${j} name)
        string(JSON property_value GET ${properties} ${j} value)
        message("${property_name} = ${property_value}")

        if (property_name STREQUAL "${TEST_PROPERTY}")
            set(property_found 1)

            if (NOT "${property_value}" STREQUAL "${EXPECTED_VALUE}")
                message(FATAL_ERROR
                    "Test '${test_name}' does not have ${TEST_PROPERTY} set to ${EXPECTED_VALUE}.\n"
                    "Found: ${property_value}"
                )
            endif()
        endif()
    endforeach()

    if(NOT property_found)
        message(FATAL_ERROR
            "Test '${test_name}' does not have ${TEST_PROPERTY} property."
        )
    endif()
endforeach()