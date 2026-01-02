from hatchling.builders.hooks.plugin.interface import BuildHookInterface

import pathlib


class BuildConfig(BuildHookInterface):
    """Builder to create and share pytest config."""

    def initialize(self, version, build_data):
        """Execute builder."""

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

        # Always accept; actual version checks are handled by FindPytest.cmake
        config_path = (build_path / "PytestConfigVersion.cmake")
        with config_path.open("w", encoding="utf-8") as stream:
            stream.write(
                "set(PACKAGE_VERSION_COMPATIBLE TRUE)\n"
                "set(PACKAGE_VERSION_EXACT TRUE)\n"
            )
