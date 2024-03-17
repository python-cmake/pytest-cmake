from hatchling.builders.hooks.plugin.interface import BuildHookInterface

import pathlib
import subprocess


class BuildConfig(BuildHookInterface):
    """Builder to create and share pytest config."""

    def initialize(self, version, build_data):
        """Execute builder."""
        import pytest

        root = pathlib.Path(__file__).parent.resolve()
        build_path = (root / "build")
        build_path.mkdir(parents=True, exist_ok=True)

        # CMake search procedure is limited to CMake package configuration files
        # and does not work with modules. Hence, we are generating a
        # configuration file based on the CMake modules created.
        # https://cmake.org/cmake/help/latest/command/find_package.html
        config_path = (build_path / "PytestConfig.cmake")
        with config_path.open("w", encoding="utf-8") as stream:
            stream.write(
                "include(${CMAKE_CURRENT_LIST_DIR}/FindPytest.cmake)\n"
            )

        # Generate CMake config version file for client to target a specific
        # version of Pytest within CMake projects.
        version_config_path = (build_path / "PytestConfigVersion.cmake")
        script_path = (build_path / "PytestConfigVersionScript.cmake")
        with script_path.open("w", encoding="utf-8") as stream:
            stream.write(
                "include(CMakePackageConfigHelpers)\n"
                "write_basic_package_version_file(\n"
                f"    \"{str(version_config_path)}\"\n"
                f"    VERSION {pytest.__version__}\n"
                "    COMPATIBILITY AnyNewerVersion\n"
                ")"
            )

        subprocess.call(["cmake", "-P", str(script_path), "-VV"])
