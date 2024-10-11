cmake_minimum_required(VERSION 3.20)

project(TestEnvironment)

find_package(Pytest 4.6.11 REQUIRED)

enable_testing()

pytest_discover_tests(
    TestEnvironment
    ENVIRONMENT
        "ENV_VAR1=VALUE1"
        "ENV_VAR2=VALUE2"
        "ENV_VAR3=PATH1:PATH2:PATH3"
)
