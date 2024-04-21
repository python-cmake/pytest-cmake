#include "./foo.h"

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdexcept>

Foo::Foo()
{
    const char* settings = std::getenv("FOO_SETTINGS_FILE");
    if (settings == nullptr) {
        throw std::runtime_error("Environment variable FOO_SETTINGS_FILE is not set.");
    }

    std::ifstream file(settings);
    if (!file.is_open()) {
        throw std::runtime_error("Unable to open Foo file.");
    }

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string lang, greeting;
        if (std::getline(iss, lang, ':') && std::getline(iss, greeting)) {
            _map[lang] = greeting;
        }
    }
    file.close();
}

std::string Foo::sayHello(std::string language)
{
    if (_map.find(language) == _map.end()) {
        throw std::runtime_error("Language not found in Foo file.");
    }

    return _map[language];
}
