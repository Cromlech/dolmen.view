# -*- coding: utf-8 -*-

# directives
from grokcore.component import Context, context, provides, name
from cromlech.io import request
from cromlech.browser import view

# components
from dolmen.view.components import View, query_view

# Import this module so that it's available as soon as you import the
# 'dolmen.view' package.  Useful for tests and interpreter examples.
import dolmen.view.testing
