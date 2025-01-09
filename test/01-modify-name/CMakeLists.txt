cmake_minimum_required(VERSION 3.20)

project(TestModifyName)

find_package(Pytest REQUIRED)

enable_testing()

pytest_discover_tests(
    TestModifyName.Simple
    DEPENDS
        strings/test_string_methods.py
        test_math_operations.py
)
set(EXPECTED
    "TestModifyName.Simple.test_inventory_keys"
    "TestModifyName.Simple.test_fruit_quantity[Fruit[banana]=150]"
    "TestModifyName.Simple.test_fruit_quantity[Fruit[apple]=100]"
    "TestModifyName.Simple.test_inventory_values"
    "TestModifyName.Simple.test_fruit_quantity[Fruit[orange]=200]"
    "TestModifyName.Simple.TestStringMethods.test_upper"
    "TestModifyName.Simple.TestStringMethods.test_lower"
    "TestModifyName.Simple.TestStringMethods.test_capitalize"
    "TestModifyName.Simple.TestStringMethods.test_split"
    "TestModifyName.Simple.test_addition"
    "TestModifyName.Simple.test_subtraction"
    "TestModifyName.Simple.test_addition_with_params[5-5-10]"
    "TestModifyName.Simple.test_addition_with_params[10-5-15]"
    "TestModifyName.Simple.test_addition_with_params[0-0-0]"
    "TestModifyName.Simple.TestStringMethods.test_strings_addition_with_params[0-0-00]"
    "TestModifyName.Simple.TestStringMethods.test_strings_addition_with_params[10-5-105]"
    "TestModifyName.Simple.TestStringMethods.test_strings_addition_with_params[5-5-55]"
)
add_test(NAME TestModifyName.Validate.Simple
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestModifyName.Simple"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestModifyName.Bundled BUNDLE_TESTS
    DEPENDS
        strings/test_string_methods.py
        test_math_operations.py

)
add_test(NAME TestModifyName.Validate.Bundled
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestModifyName.Bundled"
    -D "EXPECTED=TestModifyName.Bundled"
    -P ${CMAKE_CURRENT_LIST_DIR}/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestModifyName.TrimFromName
    TRIM_FROM_NAME "^(Test|test_)"
    DEPENDS
        strings/test_string_methods.py
        test_math_operations.py
)
set(EXPECTED
    "TestModifyName.TrimFromName.inventory_keys"
    "TestModifyName.TrimFromName.inventory_values"
    "TestModifyName.TrimFromName.fruit_quantity[Fruit[banana]=150]"
    "TestModifyName.TrimFromName.fruit_quantity[Fruit[apple]=100]"
    "TestModifyName.TrimFromName.fruit_quantity[Fruit[orange]=200]"
    "TestModifyName.TrimFromName.StringMethods.upper"
    "TestModifyName.TrimFromName.StringMethods.lower"
    "TestModifyName.TrimFromName.StringMethods.capitalize"
    "TestModifyName.TrimFromName.StringMethods.split"
    "TestModifyName.TrimFromName.addition"
    "TestModifyName.TrimFromName.subtraction"
    "TestModifyName.TrimFromName.addition_with_params[5-5-10]"
    "TestModifyName.TrimFromName.addition_with_params[10-5-15]"
    "TestModifyName.TrimFromName.addition_with_params[0-0-0]"
    "TestModifyName.TrimFromName.StringMethods.strings_addition_with_params[0-0-00]"
    "TestModifyName.TrimFromName.StringMethods.strings_addition_with_params[10-5-105]"
    "TestModifyName.TrimFromName.StringMethods.strings_addition_with_params[5-5-55]"
)
add_test(NAME TestModifyName.Validate.TrimFromName
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestModifyName.TrimFromName"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestModifyName.StripParamBrackets
    STRIP_PARAM_BRACKETS
    DEPENDS
        strings/test_string_methods.py
        test_math_operations.py
)
set(EXPECTED
    "TestModifyName.StripParamBrackets.test_inventory_keys"
    "TestModifyName.StripParamBrackets.test_inventory_values"
    "TestModifyName.StripParamBrackets.test_fruit_quantity.Fruit[banana]=150"
    "TestModifyName.StripParamBrackets.test_fruit_quantity.Fruit[apple]=100"
    "TestModifyName.StripParamBrackets.test_fruit_quantity.Fruit[orange]=200"
    "TestModifyName.StripParamBrackets.TestStringMethods.test_upper"
    "TestModifyName.StripParamBrackets.TestStringMethods.test_lower"
    "TestModifyName.StripParamBrackets.TestStringMethods.test_capitalize"
    "TestModifyName.StripParamBrackets.TestStringMethods.test_split"
    "TestModifyName.StripParamBrackets.test_addition"
    "TestModifyName.StripParamBrackets.test_subtraction"
    "TestModifyName.StripParamBrackets.test_addition_with_params.5-5-10"
    "TestModifyName.StripParamBrackets.test_addition_with_params.10-5-15"
    "TestModifyName.StripParamBrackets.test_addition_with_params.0-0-0"
    "TestModifyName.StripParamBrackets.TestStringMethods.test_strings_addition_with_params.0-0-00"
    "TestModifyName.StripParamBrackets.TestStringMethods.test_strings_addition_with_params.10-5-105"
    "TestModifyName.StripParamBrackets.TestStringMethods.test_strings_addition_with_params.5-5-55"
)
add_test(NAME TestModifyName.Validate.StripParamBrackets
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestModifyName.StripParamBrackets"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestModifyName.IncludeFilePath
    INCLUDE_FILE_PATH
    DEPENDS
        strings/test_string_methods.py
        test_math_operations.py
)
set(EXPECTED
    "TestModifyName.IncludeFilePath.data.test_sample_data.test_inventory_keys"
    "TestModifyName.IncludeFilePath.data.test_sample_data.test_inventory_values"
    "TestModifyName.IncludeFilePath.data.test_sample_data.test_fruit_quantity[Fruit[banana]=150]"
    "TestModifyName.IncludeFilePath.data.test_sample_data.test_fruit_quantity[Fruit[apple]=100]"
    "TestModifyName.IncludeFilePath.data.test_sample_data.test_fruit_quantity[Fruit[orange]=200]"
    "TestModifyName.IncludeFilePath.strings.test_string_methods.TestStringMethods.test_upper"
    "TestModifyName.IncludeFilePath.strings.test_string_methods.TestStringMethods.test_lower"
    "TestModifyName.IncludeFilePath.strings.test_string_methods.TestStringMethods.test_capitalize"
    "TestModifyName.IncludeFilePath.strings.test_string_methods.TestStringMethods.test_split"
    "TestModifyName.IncludeFilePath.test_math_operations.test_addition"
    "TestModifyName.IncludeFilePath.test_math_operations.test_subtraction"
    "TestModifyName.IncludeFilePath.test_math_operations.test_addition_with_params[5-5-10]"
    "TestModifyName.IncludeFilePath.test_math_operations.test_addition_with_params[10-5-15]"
    "TestModifyName.IncludeFilePath.test_math_operations.test_addition_with_params[0-0-0]"
    "TestModifyName.IncludeFilePath.strings.test_string_methods.TestStringMethods.test_strings_addition_with_params[0-0-00]"
    "TestModifyName.IncludeFilePath.strings.test_string_methods.TestStringMethods.test_strings_addition_with_params[10-5-105]"
    "TestModifyName.IncludeFilePath.strings.test_string_methods.TestStringMethods.test_strings_addition_with_params[5-5-55]"
)
add_test(NAME TestModifyName.Validate.IncludeFilePath
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestModifyName.IncludeFilePath"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/compare_discovered_tests.cmake
)

pytest_discover_tests(
    TestModifyName.TrimFromFullName
    TRIM_FROM_FULL_NAME "(math_|fruit_|test_)"
    INCLUDE_FILE_PATH
    DEPENDS
        strings/test_string_methods.py
        test_math_operations.py
)
set(EXPECTED
    "TestModifyName.TrimFromFullName.data.sample_data.inventory_keys"
    "TestModifyName.TrimFromFullName.data.sample_data.inventory_values"
    "TestModifyName.TrimFromFullName.data.sample_data.quantity[Fruit[banana]=150]"
    "TestModifyName.TrimFromFullName.data.sample_data.quantity[Fruit[apple]=100]"
    "TestModifyName.TrimFromFullName.data.sample_data.quantity[Fruit[orange]=200]"
    "TestModifyName.TrimFromFullName.strings.string_methods.TestStringMethods.upper"
    "TestModifyName.TrimFromFullName.strings.string_methods.TestStringMethods.lower"
    "TestModifyName.TrimFromFullName.strings.string_methods.TestStringMethods.capitalize"
    "TestModifyName.TrimFromFullName.strings.string_methods.TestStringMethods.split"
    "TestModifyName.TrimFromFullName.operations.addition"
    "TestModifyName.TrimFromFullName.operations.subtraction"
    "TestModifyName.TrimFromFullName.operations.addition_with_params[5-5-10]"
    "TestModifyName.TrimFromFullName.operations.addition_with_params[10-5-15]"
    "TestModifyName.TrimFromFullName.operations.addition_with_params[0-0-0]"
    "TestModifyName.TrimFromFullName.strings.string_methods.TestStringMethods.strings_addition_with_params[0-0-00]"
    "TestModifyName.TrimFromFullName.strings.string_methods.TestStringMethods.strings_addition_with_params[10-5-105]"
    "TestModifyName.TrimFromFullName.strings.string_methods.TestStringMethods.strings_addition_with_params[5-5-55]"
)
add_test(NAME TestModifyName.Validate.TrimFromFullName
    COMMAND ${CMAKE_COMMAND}
    -D "TEST_PREFIX=TestModifyName.TrimFromFullName"
    -D "EXPECTED=${EXPECTED}"
    -P ${CMAKE_CURRENT_LIST_DIR}/compare_discovered_tests.cmake
)
