from setuptools import setup
import pathlib
import shutil
import tempfile

root = pathlib.Path(__file__).parent.resolve()
long_description = (root / "README.md").read_text(encoding="utf-8")

# Copy the Pytest module to be fetched as a config.
temp_dir = pathlib.Path(tempfile.gettempdir())

config_path = str(temp_dir / "PytestConfig.cmake")
shutil.copy(str(root / "cmake" / "FindPytest.cmake"), config_path)

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
            [config_path, "cmake/PytestAddTests.cmake"]
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
