# -*- coding: utf-8 -*-

import unittest
import doctest
import zope.component.hooks
from pkg_resources import resource_listdir

optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS


def setUp(*args, **kwargs):
    zope.component.hooks.setHooks()


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
        dottedname = 'dolmen.view.tests.%s.%s' % (name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            setUp=setUp,
            optionflags=optionflags)
        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['view']:
        suite.addTest(suiteFromPackage(name))
    return suite
