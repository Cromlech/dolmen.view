# -*- coding: utf-8 -*-

import crom
from crom import testing
from crom.implicit import implicit
from cromlech.browser import IView
from cromlech.browser.testing import TestRequest


class Context(object):
    pass


context = Context
request = TestRequest()


def setup_function(method):
    testing.setup()


def teardown_function(method):
    testing.teardown()


def test_component():
    from .fixtures import base_view as module

    # grok the component module
    crom.configure(module)

    # we should now be able to adapt things
    assert implicit.registry.lookup(
        (context, request), IView, 'uselessrock') is module.UselessRock

