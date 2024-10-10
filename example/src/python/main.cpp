#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <foo.h>

#include <cstdlib>
#include <string>

namespace nb = nanobind;

std::string greet(const std::string& name = "world")
{
    Foo foo;

    const char* value = std::getenv("DEFAULT_LANGUAGE");
    if (value != nullptr)
        return foo.sayHello(value) + ", " + name;
    else
        return foo.sayHello("fr") + ", " + name;
}

NB_MODULE(foo, m)
{
    m.def("greet", &greet, nb::arg("name") = "world");
}
