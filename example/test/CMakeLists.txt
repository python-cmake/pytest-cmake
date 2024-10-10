pytest_discover_tests(
    PythonTest
    LIBRARY_PATH_PREPEND
        $<TARGET_FILE_DIR:foo>
        $<TARGET_FILE_DIR:pyFoo>
    PYTHON_PATH_PREPEND
        $<TARGET_FILE_DIR:pyFoo>
    TRIM_FROM_NAME "^(Test|test_)"
    STRIP_PARAM_BRACKETS
    INCLUDE_FILE_PATH
    DEPENDS foo pyFoo
    ENVIRONMENT
        "DEFAULT_LANGUAGE=en"
        "FOO_SETTINGS_FILE=${CMAKE_CURRENT_SOURCE_DIR}/resource/foo.txt"
)

if (WIN32)
    # Expand functions to copy dependent DLLs in the same folder after
    # building target to ensure that tests can run properly on Windows.
    macro(add_test NAME)
        add_custom_command(
            TARGET ${NAME} POST_BUILD
            COMMAND ${CMAKE_COMMAND}
            -E copy_if_different
            $<TARGET_RUNTIME_DLLS:${NAME}>
            $<TARGET_FILE_DIR:${NAME}>
            COMMAND_EXPAND_LISTS
        )
        _add_test(${NAME} ${ARGV})
    endmacro()
endif()

add_executable(CppTest fooTest.cpp)
target_link_libraries(CppTest foo)
add_test(CppTest CppTest)
set_tests_properties(
    CppTest
    PROPERTIES ENVIRONMENT
        "FOO_SETTINGS_FILE=${CMAKE_CURRENT_SOURCE_DIR}/resource/foo.txt"
)
