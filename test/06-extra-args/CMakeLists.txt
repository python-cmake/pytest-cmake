cmake_minimum_required(VERSION 3.20)

project(TestExtraArgs)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestExtraArgs
    EXTRA_ARGS "--capture=no" "--cmdopt=demo"
)

pytest_discover_tests(
    TestDiscoveryExtraArgs.IgnoreCustomArgs
    EXTRA_ARGS "--capture=no"
    DISCOVERY_EXTRA_ARGS "--ignore=custom_args"
)

pytest_discover_tests(
    TestDiscoveryExtraArgs.OnlyCustomArgs
    EXTRA_ARGS "--cmdopt=demo"
    DISCOVERY_EXTRA_ARGS "-k=custom"
)

pytest_discover_tests(
    TestDiscoveryExtraArgs.OnlyCustomArgsBundled
    EXTRA_ARGS "--cmdopt=demo"
    DISCOVERY_EXTRA_ARGS "-k=custom"
    BUNDLE_TESTS
)
