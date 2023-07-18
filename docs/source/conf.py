# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
sys.path.insert(0, "/home/tumpa/Projects/yadis-discord-bot/src")
os.chdir("")

project = 'Yadis'
copyright = '2023, Tumpa-Prizrak'
author = 'Tumpa-Prizrak'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']

autosummary_generate = True
autosummary_imported_members = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'haiku'
html_static_path = ['_static']
"""html_theme_options = {
    "footerbgcolor": "#2b2b2e",
    "footertextcolor": "#b9b6d1",
    "sidebarbgcolor": "#2c2c34",
    "sidebartextcolor": "#777170",
    "sidebarlinkcolor": "#6aae87",
    "relbarbgcolor": "#36577c",
    "relbartextcolor": "#3c74ac",
    "relbarlinkcolor": "#728bda",
    "bgcolor": "#1c1c24",
    "textcolor": "#b9b6d1",
    "linkcolor": "#606a74",
    "visitedlinkcolor": "#3d5771",
    "headbgcolor": "#2e3434",
    "headtextcolor": "#FFF",
    "headlinkcolor": "#3e2e34",
    "codebgcolor": "#1c1d25",
    "codetextcolor": "#ffffb1",
    "bodyfont": "Arial",
    "headfont": "Comic Sans"
}
"""