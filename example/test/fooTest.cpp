#include "foo.h"

int main() {
    Foo foo;
    return foo.sayHello("en") == "hello" ? 0 : 1;
}
