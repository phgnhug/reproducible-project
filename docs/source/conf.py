"""Sphinx configuration for House Price Predictor documentation."""

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "House Price Predictor"
copyright = "2026, Nhung Nguyen, Chau Phan, Sherry"
author = "Nhung Nguyen, Chau Phan, Sherry"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
