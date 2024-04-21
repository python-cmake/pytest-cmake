add_library(pyFoo MODULE main.cpp)

set_target_properties(pyFoo
    PROPERTIES
        PREFIX ""
        OUTPUT_NAME foo
)

if(WIN32)
    set_target_properties(pyFoo PROPERTIES SUFFIX ".pyd")
endif()

target_link_libraries(pyFoo
    PUBLIC
        foo
        Boost::python
        Python::Python
)

if (WIN32)
    # As of Python v3.8 and newer, DLLs are no longer searched for in the 
    # PATH environment variable on Windows. Therefore, it is necessary to
    # ensure that they are all located in the same directory.
    add_custom_command(
        TARGET pyFoo POST_BUILD
        COMMAND ${CMAKE_COMMAND}
        -E copy_if_different
        $<TARGET_FILE:foo>
        $<TARGET_FILE_DIR:pyFoo>
        COMMAND_EXPAND_LISTS
    )
endif()
