pytest_discover_tests(
    PythonTest
    LIBRARY_PATH_PREPEND
        $<TARGET_FILE_DIR:foo>
        $<TARGET_FILE_DIR:pyFoo>
    PYTHON_PATH_PREPEND
        $<TARGET_FILE_DIR:pyFoo>
    TRIM_FROM_NAME "^(Test|test_)"
    DEPENDS foo pyFoo
    ENVIRONMENT
        "DEFAULT_LANGUAGE=en"
        "FOO_SETTINGS_FILE=${CMAKE_CURRENT_SOURCE_DIR}/resource/foo.txt"
)
