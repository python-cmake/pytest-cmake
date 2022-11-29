from setuptools import setup
import pytest

import pathlib
import subprocess
import tempfile

root = pathlib.Path(__file__).parent.resolve()
long_description = (root / "README.md").read_text(encoding="utf-8")

temp_dir = pathlib.Path(tempfile.mkdtemp(prefix="pytest-cmake-"))

# CMake search procedure is limited to CMake package configuration files and
# does not work with modules. Hence, we are generating a configuration file
# based on the CMake modules created.
# https://cmake.org/cmake/help/latest/command/find_package.html
config_path = (temp_dir / "PytestConfig.cmake")
with config_path.open("w", encoding="utf-8") as stream:
    stream.write("include(${CMAKE_CURRENT_LIST_DIR}/FindPytest.cmake)\n")

# Generate CMake config version file for client to target a specific version
# of Pytest within CMake projects.
# https://cmake.org/cmake/help/latest/module/CMakePackageConfigHelpers.html
version_config_path = (temp_dir / "PytestConfigVersion.cmake")
script_path = (temp_dir / "PytestConfigVersionScript.cmake")
with script_path.open("w", encoding="utf-8") as stream:
    stream.write(
        "include(CMakePackageConfigHelpers)\n"
        "write_basic_package_version_file(\n"
        f"    \"{str(version_config_path)}\"\n"
        f"    VERSION {pytest.__version__}\n"
        "    COMPATIBILITY AnyNewerVersion\n"
        ")"
    )

subprocess.call(["cmake", "-P", str(script_path)])

# Python package configuration in charge of installing CMake configuration files
# where CMake search procedure can discover it.
setup(
    name="pytest-cmake",
    version="0.1.0",
    description="Provide CMake module for Pytest",
    long_description=long_description,
    keywords="cmake, pytest, development",
    python_requires=">=3.7, <4",
    data_files=[
        (
            "share/Pytest/cmake",
            [
                str(config_path),
                str(version_config_path),
                "cmake/FindPytest.cmake",
                "cmake/PytestAddTests.cmake"
            ]
        )
    ],
    install_requires=["pytest >= 4, < 8"],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
