# -*- coding: utf-8 -*-

from zope.configuration.config import ConfigurationMachine
from grokcore.component import zcml


def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok('grokcore.component.meta', config)
    zcml.do_grok('grokcore.security.meta', config)
    zcml.do_grok('dolmen.view.meta', config)
    zcml.do_grok('dolmen.view.security', config)
    zcml.do_grok('cromlech.webob', config)
    zcml.do_grok(module_name, config)
    config.execute_actions()
