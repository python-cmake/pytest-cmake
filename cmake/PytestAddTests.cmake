# Wrapper used to create individual CTest tests from Pytest tests.
cmake_minimum_required(VERSION 3.20...3.29)

if(CMAKE_SCRIPT_MODE_FILE)

    # Set Cmake test file to execute each test.
    set(_content "")

    # Ensure that list environment variables are
    # represented as a string on Windows.
    string(REPLACE [[;]] [[\;]] LIBRARY_PATH "${LIBRARY_PATH}")
    string(REPLACE [[;]] [[\;]] PYTHON_PATH "${PYTHON_PATH}")

    if (BUNDLE_TESTS)
        string(APPEND _content
            "add_test(\n"
            "    \"${TEST_GROUP_NAME}\"\n"
            "    ${PYTEST_EXECUTABLE} \"${WORKING_DIRECTORY}\"\n"
            ")\n"
            "set_tests_properties(\n"
            "     \"${TEST_GROUP_NAME}\" PROPERTIES\n"
            "     ENVIRONMENT \"${LIB_ENV_PATH}=${LIBRARY_PATH}\"\n"
            ")\n"
            "set_tests_properties(\n"
            "     \"${TEST_GROUP_NAME}\"\n"
            "     APPEND PROPERTIES\n"
            "     ENVIRONMENT \"PYTHONPATH=${PYTHON_PATH}\"\n"
            ")\n"
        )

        foreach(env ${ENVIRONMENT})
            string(APPEND _content
                "set_tests_properties(\n"
                "     \"${TEST_GROUP_NAME}\"\n"
                "     APPEND PROPERTIES\n"
                "     ENVIRONMENT ${env}\n"
                ")\n"
            )
        endforeach()

    else()
        # Set environment for collecting tests.
        set(ENV{${LIB_ENV_PATH}} "${LIBRARY_PATH}")
        set(ENV{PYTHONPATH} "${PYTHON_PATH}")
        set(ENV{PYTHONWARNINGS} "ignore")

        execute_process(
            COMMAND "${PYTEST_EXECUTABLE}"
                --collect-only -q
                --rootdir=${WORKING_DIRECTORY} .
            OUTPUT_VARIABLE _output_lines
            ERROR_VARIABLE _output_lines
            OUTPUT_STRIP_TRAILING_WHITESPACE
            WORKING_DIRECTORY ${WORKING_DIRECTORY}
        )

        string(REGEX MATCH "=+ ERRORS =+(.*)" _error ${_output_lines})

        if (_error)
            message(${_error})
            message(FATAL_ERROR "An error occurred during the collection of Python tests.")
        endif()

        # Convert output into list.
        string(REPLACE [[;]] [[\;]] _output_lines "${_output_lines}")
        string(REPLACE "\n" ";" _output_lines "${_output_lines}")

        set(test_pattern "([^:]+)(::([^:]+))?::([^:]+)")

        foreach (line ${_output_lines})
            string(REGEX MATCHALL ${test_pattern} matching "${line}")

            # Ignore lines not identified as a test.
            if (NOT matching)
                continue()
            endif()

            set(_class ${CMAKE_MATCH_3})
            set(_func ${CMAKE_MATCH_4})

            if (_class)
                set(test_name "${_class}.${_func}")
            else()
                set(test_name "${_func}")
            endif()

            if (TRIM_FROM_NAME)
                string(REGEX REPLACE
                        "${TRIM_FROM_NAME}" "" test_name "${test_name}")
            endif()

            set(test_name "${TEST_GROUP_NAME}.${test_name}")
            set(test_case "${WORKING_DIRECTORY}/${line}")

            string(APPEND _content
                "add_test(\n"
                "    \"${test_name}\"\n"
                "    ${PYTEST_EXECUTABLE} \"${test_case}\"\n"
                ")\n"
                "set_tests_properties(\n"
                "     \"${test_name}\" PROPERTIES\n"
                "     ENVIRONMENT \"${LIB_ENV_PATH}=${LIBRARY_PATH}\"\n"
                ")\n"
                "set_tests_properties(\n"
                "     \"${test_name}\"\n"
                "     APPEND PROPERTIES\n"
                "     ENVIRONMENT \"PYTHONPATH=${PYTHON_PATH}\"\n"
                ")\n"
            )

            foreach(env ${ENVIRONMENT})
                string(APPEND _content
                    "set_tests_properties(\n"
                    "     \"${test_name}\"\n"
                    "     APPEND PROPERTIES\n"
                    "     ENVIRONMENT ${env}\n"
                    ")\n"
                )
            endforeach()

        endforeach()

        if(NOT _content)
            message(WARNING "No Python tests have been discovered.")
        endif()
    endif()

    file(WRITE ${CTEST_FILE} ${_content})
endif()
