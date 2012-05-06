# -*- coding: utf-8 -*-

from zope.configuration.config import ConfigurationMachine
from grokcore.component import zcml

try:
    import grokcore.security
    HAS_SECURITY = True
except ImportError:
    HAS_SECURITY = False


def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok('grokcore.component.meta', config)
    zcml.do_grok('dolmen.view.meta', config)
    if HAS_SECURITY:
        zcml.do_grok('grokcore.security.meta', config)
        zcml.do_grok('dolmen.view.security', config)
    zcml.do_grok(module_name, config)
    config.execute_actions()
