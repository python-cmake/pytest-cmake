"""Custom backend to ensure compatibility with Python 2.7.
"""

import sys

if sys.version_info[0] < 3:
    from setuptools.build_meta import *
else:
    from hatchling.build import *
