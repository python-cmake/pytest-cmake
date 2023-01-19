"""Setuptools config only used for Python 2.7 compatibility.
"""

from setuptools import setup
from setuptools.command.build_py import build_py

import os
import subprocess


ROOT = os.path.dirname(os.path.realpath(__file__))


class BuildExtended(build_py):
    """Custom command to create and share pytest config."""

    def run(self):
        """Execute builder."""
        import pytest

        build_path = os.path.join(ROOT, "build")
        if not os.path.exists(build_path):
            os.makedirs(build_path)

        # CMake search procedure is limited to CMake package configuration files
        # and does not work with modules. Hence, we are generating a
        # configuration file based on the CMake modules created.
        # https://cmake.org/cmake/help/latest/command/find_package.html
        config_path = os.path.join(build_path, "PytestConfig.cmake")
        with open(config_path, "w") as stream:
            stream.write(
                "include(${CMAKE_CURRENT_LIST_DIR}/FindPytest.cmake)\n"
            )

        # Generate CMake config version file for client to target a specific
        # version of Pytest within CMake projects.
        version_config_path = os.path.join(
            build_path, "PytestConfigVersion.cmake"
        )
        script_path = os.path.join(
            build_path, "PytestConfigVersionScript.cmake"
        )
        with open(script_path, "w") as stream:
            stream.write(
                "include(CMakePackageConfigHelpers)\n"
                "write_basic_package_version_file(\n"
                "    \"{path}\"\n"
                "    VERSION {version}\n"
                "    COMPATIBILITY AnyNewerVersion\n"
                ")".format(
                    path=str(version_config_path),
                    version=pytest.__version__,
                )
            )

        subprocess.call(["cmake", "-P", str(script_path), "-VV"])


setup(
    name="pytest-cmake",
    version="0.1.0",
    data_files=[
        (
            "share/Pytest/cmake",
            [
                "build/PytestConfig.cmake",
                "build/PytestConfigVersion.cmake",
                "cmake/FindPytest.cmake",
                "cmake/PytestAddTests.cmake"
            ]
        )
    ],
    cmdclass={"build_py": BuildExtended},
    install_requires=["pytest >= 4, < 8"],
)
