#include <boost/python.hpp>

#include <cstdlib>
#include <string>

std::string greet(std::string name)
{
    const char* value = std::getenv("GREETING_WORD");
    if (value != nullptr)
        return std::string(value) + ", " + name;
    else
        return "bonjour, " + name;
}

BOOST_PYTHON_MODULE(example)
{
    using namespace boost::python;
    Py_Initialize();

    def("greet", greet, arg("name") = "world");
}
