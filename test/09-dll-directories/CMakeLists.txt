cmake_minimum_required(VERSION 3.20)

project(TestDllDirectories)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestDllDirectories
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
)
