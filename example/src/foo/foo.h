#ifndef EXAMPLE_FOO_H
#define EXAMPLE_FOO_H

#include <string>
#include <unordered_map>

class Foo {
public:
    Foo();
    virtual ~Foo() = default;

    std::string sayHello(std::string language);

private:
    std::unordered_map<std::string, std::string> _map;
};

#endif // EXAMPLE_FOO_H
