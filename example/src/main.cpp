#include <boost/python.hpp>

#include <string>

std::string greet(std::string name)
{
    return "hello, " + name;
}

BOOST_PYTHON_MODULE(example)
{
    using namespace boost::python;
    Py_Initialize();

    def("greet", greet, arg("name") = "world");
}
