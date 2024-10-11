cmake_minimum_required(VERSION 3.20)

project(TestLibraryPath)

find_package(Pytest 4.6.11 REQUIRED)

enable_testing()

if(WIN32)
    set(EXPECTED "\\path")
else()
    set(EXPECTED "/path")
endif()
configure_file(test_path.py "test1/test_path.py" @ONLY)

pytest_discover_tests(
    TestLibraryPath.AddOne
    LIBRARY_PATH_PREPEND "/path"
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/test1"
)

if(WIN32)
    set(EXPECTED "\\path1;\\path2;\\path3")
else()
    set(EXPECTED "/path1:/path2:/path3")
endif()
configure_file(test_path.py "test2/test_path.py" @ONLY)

pytest_discover_tests(
    TestLibraryPath.AddSeveral
    LIBRARY_PATH_PREPEND "/path1" "/path2" "/path3"
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/test2"
)
