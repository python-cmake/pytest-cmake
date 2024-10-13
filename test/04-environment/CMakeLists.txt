cmake_minimum_required(VERSION 3.20)

project(TestEnvironment)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestEnvironment
    ENVIRONMENT
        "KEY1=VALUE1"
        "KEY2=VALUE2"
        "KEY3=PATH1:PATH2:PATH3"
        "KEY4=PATH1\;PATH2\;PATH3"
        "KEY5=C:\\Path\\To\\Dir1\;C:\\Path\\To\\Dir2"
        "K3Y4=SPECIAL$VALUE!@#%^&*"
)
