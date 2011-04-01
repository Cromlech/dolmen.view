# -*- coding: utf-8 -*-

import martian
from zope.interface import Interface

class view(martian.Directive):
    scope = martian.CLASS_OR_MODULE
    store = martian.ONCE
    default = Interface