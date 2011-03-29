# -*- coding: utf-8 -*-

import re
import unittest
from pkg_resources import resource_listdir
from zope.testing import doctest, cleanup, renormalizing
import zope.component.eventtesting
from grokcore.view.templatereg import file_template_registry

optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS


def suiteFromPackage(name):
    files = resource_listdir(__name__, name)
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename.endswith('_fixture.py'):
            continue
        if filename == '__init__.py':
            continue
        dottedname = 'grokcore.view.tests.%s.%s' % (name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            optionflags=optionflags)
        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['view']:
        suite.addTest(suiteFromPackage(name))
    return suite
