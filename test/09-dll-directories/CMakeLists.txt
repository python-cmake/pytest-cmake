cmake_minimum_required(VERSION 3.20)

project(TestDllDirectories)

find_package(Pytest REQUIRED)

enable_testing()

# A DEPENDS target used purely for build ordering, with no runtime DLLs of
# its own: TARGET_RUNTIME_DLL_DIRS cannot be evaluated on it, so it must be
# skipped rather than passed through and fail CMake generation.
add_library(NonBinaryDependency INTERFACE)

pytest_discover_tests(
    TestDllDirectories
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    DEPENDS NonBinaryDependency
)
