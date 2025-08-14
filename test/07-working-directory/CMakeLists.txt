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
