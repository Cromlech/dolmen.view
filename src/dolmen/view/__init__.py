# -*- coding: utf-8 -*-

from grokcore.component import *
from dolmen.view.components import View, ViewSupport, TemplateView
from dolmen.view.directive import request, view

# Import this module so that it's available as soon as you import the
# 'dolmen.view' package.  Useful for tests and interpreter examples.
import dolmen.view.testing
