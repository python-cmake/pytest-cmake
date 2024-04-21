add_library(foo SHARED foo.cpp)

target_include_directories(foo
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
)
