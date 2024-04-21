#include <boost/python.hpp>
#include <foo.h>

#include <cstdlib>
#include <string>

std::string greet(std::string name)
{
    Foo foo;

    const char* value = std::getenv("DEFAULT_LANGUAGE");
    if (value != nullptr)
        return foo.sayHello(value) + ", " + name;
    else
        return foo.sayHello("fr") + ", " + name;
}

BOOST_PYTHON_MODULE(foo)
{
    using namespace boost::python;
    Py_Initialize();

    def("greet", greet, arg("name") = "world");
}
