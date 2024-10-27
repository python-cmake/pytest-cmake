# -*- coding: utf-8 -*-

"""Documentation build configuration file."""

import re
import pathlib
import sys

root = pathlib.Path(__file__).parent.resolve()
sys.path.insert(0, str(root / "_extensions"))

# -- General ------------------------------------------------------------------

# Extensions.
extensions = ["changelog", "github_user", "sphinx.ext.intersphinx"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Pytest CMake"
copyright = u"2022, Jeremy Retailleau"

# Version
pattern = r"version = \"([\d\\.]+)\""
config = (root.parent / "pyproject.toml").read_text(encoding="utf-8")

version = re.search(pattern, config, re.DOTALL).group(1)
release = version

# -- HTML output --------------------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_favicon = "favicon.ico"
html_static_path = ["_static"]
html_css_files = ["style.css"]
html_copy_source = True

# -- Intersphinx --------------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
