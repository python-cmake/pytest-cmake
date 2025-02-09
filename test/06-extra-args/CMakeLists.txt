cmake_minimum_required(VERSION 3.20)

project(TestExtraArgs)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestExtraArgs
    EXTRA_ARGS "--capture=no" "--cmdopt=demo"
    DEPENDS test_extra_args.py
)
