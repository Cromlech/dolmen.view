# -*- coding: utf-8 -*-

import martian
from zope.interface import Interface
from zope.interface.interfaces import IInterface
from cromlech.io.interfaces import IRequest


def validateRequest(directive, value):
    martian.validateInterfaceOrClass(directive, value)
    if IInterface.providedBy(value):
        if not IRequest.isOrExtends(value):
            raise GrokImportError(
                "%r is not a valid `IRequest` interface." % value)
    else:
        if not IRequest.implementedBy(value):
            raise GrokImportError(
                "%r must implemented the `IRequest` interface." % value)
        

class view(martian.Directive):
    scope = martian.CLASS_OR_MODULE
    store = martian.ONCE
    default = Interface


class request(martian.Directive):
    scope = martian.CLASS_OR_MODULE
    store = martian.ONCE
    default = Interface
