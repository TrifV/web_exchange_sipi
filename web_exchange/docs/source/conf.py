import os
import sys
# уровень выше — корень проекта
sys.path.insert(0, os.path.abspath('/Users/vadim_trifonov/Desktop/web_exchange/app'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'web_exchange'
copyright = '2025, Trifonov_Fomin_Shencev'
author = 'Trifonov_Fomin_Shencev'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # автодокументация по docstring
    'sphinx.ext.viewcode',   # вывод исходников
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
