nanobind_add_module(pyFoo main.cpp)

set_target_properties(pyFoo
    PROPERTIES
        PREFIX ""
        SUFFIX ".so"
        OUTPUT_NAME foo
)

if(WIN32)
    set_target_properties(pyFoo PROPERTIES SUFFIX ".pyd")
endif()

target_link_libraries(pyFoo PUBLIC foo)
