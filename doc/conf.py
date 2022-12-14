# -*- coding: utf-8 -*-

"""Documentation build configuration file."""

import re
import pathlib

# -- General ------------------------------------------------------------------

# Extensions.
extensions = ["lowdown", "sphinx.ext.intersphinx"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Pytest CMake"
copyright = u"2022, Jeremy Retailleau"

# Version
pattern = r"version = \"([\d\\.]+)\""
root = pathlib.Path(__file__).parent.resolve()
config = (root.parent / "pyproject.toml").read_text(encoding="utf-8")

version = re.search(pattern, config, re.DOTALL).group(1)
release = version

# -- HTML output --------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

# If True, copy source rst files to output for reference.
html_copy_source = True

# -- Intersphinx --------------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
