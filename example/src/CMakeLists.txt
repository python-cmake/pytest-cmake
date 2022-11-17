add_library(example MODULE main.cpp)

set_target_properties(example PROPERTIES PREFIX "")

if(WIN32)
    set_target_properties(example PROPERTIES SUFFIX ".pyd")
endif()

target_link_libraries(example PUBLIC Boost::python Python::Python)
