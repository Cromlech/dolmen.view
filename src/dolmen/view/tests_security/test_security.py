# -*- coding: utf-8 -*-

import doctest
import unittest
import dolmen.view
from zope.component.testlayer import ZCMLFileLayer

FLAGS = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
layer = ZCMLFileLayer(dolmen.view.tests_security)


def test_suite():
    """Get a testsuite of all doctests.
    """
    suite = unittest.TestSuite()
    for name in ['security.txt']:
        test = doctest.DocFileSuite(
            name,
            package=dolmen.view.tests_security,
            optionflags=FLAGS,
            )
        suite.addTest(test)
    suite.layer = layer
    return suite
