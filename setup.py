from setuptools import setup
import pytest

import pathlib
import tempfile

root = pathlib.Path(__file__).parent.resolve()
long_description = (root / "README.md").read_text(encoding="utf-8")

# Copy the Pytest module to be fetched as a config.
temp_dir = pathlib.Path(tempfile.gettempdir())

config_path = (temp_dir / "PytestConfig.cmake")
with config_path.open("w", encoding="utf-8") as stream:
    stream.write("include(${CMAKE_CURRENT_LIST_DIR}/FindPytest.cmake)")

version_config_path = (temp_dir / "PytestConfigVersion.cmake")
with version_config_path.open("w", encoding="utf-8") as stream:
    stream.write(
        f"set(PACKAGE_VERSION \"{pytest.__version__}\")\n"
        "\n"
        "if (PACKAGE_FIND_VERSION_RANGE)\n"
        "  # Package version must be in the requested version range\n"
        "  if ((PACKAGE_FIND_VERSION_RANGE_MIN STREQUAL \"INCLUDE\" AND "
        "PACKAGE_VERSION VERSION_LESS PACKAGE_FIND_VERSION_MIN)\n"
        "      OR ((PACKAGE_FIND_VERSION_RANGE_MAX STREQUAL \"INCLUDE\" AND "
        "PACKAGE_VERSION VERSION_GREATER PACKAGE_FIND_VERSION_MAX)\n"
        "        OR (PACKAGE_FIND_VERSION_RANGE_MAX STREQUAL \"EXCLUDE\" AND "
        "PACKAGE_VERSION VERSION_GREATER_EQUAL PACKAGE_FIND_VERSION_MAX)))\n"
        "    set(PACKAGE_VERSION_COMPATIBLE FALSE)\n"
        "  else()\n"
        "    set(PACKAGE_VERSION_COMPATIBLE TRUE)\n"
        "  endif()\n"
        "else()\n"
        "  if(PACKAGE_VERSION VERSION_LESS PACKAGE_FIND_VERSION)\n"
        "    set(PACKAGE_VERSION_COMPATIBLE FALSE)\n"
        "  else()\n"
        "    set(PACKAGE_VERSION_COMPATIBLE TRUE)\n"
        "    if(PACKAGE_FIND_VERSION STREQUAL PACKAGE_VERSION)\n"
        "      set(PACKAGE_VERSION_EXACT TRUE)\n"
        "    endif()\n"
        "  endif()\n"
        "endif()\n"
    )

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
