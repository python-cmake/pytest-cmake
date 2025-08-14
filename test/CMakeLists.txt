cmake_minimum_required(VERSION 3.20)

project(Test)

include(ExternalProject)

ExternalProject_Add(
    TestModifyName
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/01-modify-name
    BINARY_DIR ${CMAKE_BINARY_DIR}/_deps/01-modify-name
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND}
        -C Release -VV
        -R ModifyName.Validate
)

ExternalProject_Add(
    TestLibraryPath
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/02-library-path
    BINARY_DIR ${CMAKE_BINARY_DIR}/_deps/02-library-path
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND} -C Release -VV
)

ExternalProject_Add(
    TestPythonPath
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/03-python-path
    BINARY_DIR ${CMAKE_BINARY_DIR}/_deps/03-python-path
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND} -C Release -VV
)

ExternalProject_Add(
    TestEnvironment
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/04-environment
    BINARY_DIR ${CMAKE_BINARY_DIR}/_deps/04-environment
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND} -C Release -VV
)

ExternalProject_Add(
    TestProperties
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/05-properties
    BINARY_DIR ${CMAKE_BINARY_DIR}/_deps/05-properties
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND}
        -C Release -VV
        -R TestProperties.Validate
)

ExternalProject_Add(
    TestExtraArgs
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/06-extra-args
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/_deps/06-extra-args
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND}
        -C Release -VV
)

ExternalProject_Add(
    TestWorkingDirectory
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/07-working-directory
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/_deps/07-working-directory
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND}
        -C Release -VV
)

ExternalProject_Add(
    TestCustomPaths
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/08-test-paths
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/_deps/08-test-paths
    BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR>
    INSTALL_COMMAND ""
    TEST_COMMAND ${CMAKE_CTEST_COMMAND}
        -C Release -VV
)
