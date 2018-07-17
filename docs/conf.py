# -*- coding: utf-8 -*-

import sys
import os

# -- General configuration ------------------------------------------------

extensions = []

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'HCL Welcome Pack'
copyright = u'2018, HCL'

version = '1.0'
release = '1.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'ReadtheDocsTemplatedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

}

latex_documents = [
  ('index', 'ReadtheDocsTemplate.tex', u'Read the Docs Template Documentation',
   u'Read the Docs', 'manual'),
]


# -- Options for manual page output ---------------------------------------

section).
man_pages = [
    ('index', 'readthedocstemplate', u'Read the Docs Template Documentation',
     [u'Read the Docs'], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
  ('index', 'ReadtheDocsTemplate', u'Read the Docs Template Documentation',
   u'Read the Docs', 'ReadtheDocsTemplate', 'One line description of project.',
   'Miscellaneous'),
]