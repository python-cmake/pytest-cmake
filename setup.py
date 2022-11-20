from setuptools import setup
import pathlib

root = pathlib.Path(__file__).parent.resolve()
long_description = (root / "README.md").read_text(encoding="utf-8")

setup(
    name="pytest-cmake",
    version="0.1.0",
    description="Provide CMake module for Pytest",
    long_description=long_description,
    keywords="cmake, pytest, development",
    python_requires=">=3.7, <4",
    data_files=[
        (
            "share/cmake/Modules",
            ["cmake/FindPytest.cmake", "cmake/PytestAddTests.cmake"]
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
