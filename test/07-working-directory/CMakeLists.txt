cmake_minimum_required(VERSION 3.20)

project(TestWorkingDirectory)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestWorkingDirectory
    WORKING_DIRECTORY subdir
)

pytest_discover_tests(
    TestWorkingDirectory.Bundled
    WORKING_DIRECTORY subdir
    BUNDLE_TESTS
)

# Link to this directory, using a junction on Windows as it does not require
# elevated privileges.
set(_link "${CMAKE_CURRENT_BINARY_DIR}/link")
if (NOT EXISTS "${_link}")
    if (WIN32)
        file(TO_NATIVE_PATH "${_link}" _native_link)
        file(TO_NATIVE_PATH "${CMAKE_CURRENT_SOURCE_DIR}" _native_target)
        execute_process(
            COMMAND cmd /c mklink /J "${_native_link}" "${_native_target}"
            OUTPUT_QUIET
            COMMAND_ERROR_IS_FATAL ANY
        )
    else()
        file(CREATE_LINK "${CMAKE_CURRENT_SOURCE_DIR}" "${_link}" SYMBOLIC)
    endif()
endif()

# Tests should run from the linked path. Collection must still succeed, without
# loading the conftest file from the parent of the resolved path.
pytest_discover_tests(
    TestWorkingDirectory.Link.Simple
    WORKING_DIRECTORY "${_link}/subdir"
)

pytest_discover_tests(
    TestWorkingDirectory.Link.Bundled
    WORKING_DIRECTORY "${_link}/subdir"
    BUNDLE_TESTS
)

foreach (_variant IN ITEMS Simple Bundled)
    add_test(NAME TestWorkingDirectory.Validate.Link.${_variant}
        COMMAND ${CMAKE_COMMAND}
        -D "TEST_PREFIX=TestWorkingDirectory.Link.${_variant}"
        -D "TEST_PROPERTY=WORKING_DIRECTORY"
        -D "EXPECTED_VALUE=${_link}/subdir"
        -P ${CMAKE_CURRENT_LIST_DIR}/../utils/check_test_property.cmake
    )
endforeach()
