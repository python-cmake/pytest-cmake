import argparse
from pathlib import Path
import sys
import sysconfig


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="pytest-cmake",
        description="Utility commands for pytest-cmake packaging.",
    )
    parser.add_argument(
        "--cmake_dir", "--cmake-dir",
        action="store_true",
        help="Print the CMake config directory path and exit.",
    )
    args = parser.parse_args(argv)

    if args.cmake_dir:
        data_root = Path(sysconfig.get_path("data"))
        print(data_root / "share" / "Pytest" / "cmake")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
