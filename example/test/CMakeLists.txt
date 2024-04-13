pytest_discover_tests(
    PythonTest
    LIBRARY_PATH_PREPEND
        $ENV{RUNNER_TEMP}
        $<TARGET_FILE_DIR:example>
    PYTHON_PATH_PREPEND
        $ENV{RUNNER_TEMP}
        $<TARGET_FILE_DIR:example>
    TRIM_FROM_NAME "^test_"
    DEPENDS example
    ENVIRONMENT
        "GREETING_WORD=hello"
)
