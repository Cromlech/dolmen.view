# -*- coding: utf-8 -*-

from grokker import grokker, directive, Directive
from crom.directives import sources, target, name
from crom.implicit import implicit
from crom.interfaces import IRegistry, NoImplicitRegistryError
from crom.grokkers import registry
from cromlech.browser import IView, IRequest
from grokker import Directive, validator
from zope.interface import implementer, Interface
from crom.validators import class_or_interface_validator, interface_validator


context = Directive(
    'context', 'cromlech', validator=class_or_interface_validator)

request = Directive(
    'request', 'cromlech', validator=class_or_interface_validator)


@grokker
@directive(context)
@directive(request)
@directive(target)
@directive(name)
@directive(registry)
def view_component(scanner, pyname,
         obj, registry,
         target=IView, context=Interface, request=IRequest, name=None):

    if name is None:
        name = obj.__name__.lower()

    print obj, registry, target, context, request, name
    obj.__component_name__ = name

    assert target.isOrExtends(IView)

    def register():
        registry.register((context, request), target, name, obj)

    scanner.config.action(
        discriminator=('view', (context, request), target, name, registry),
        callable=register
        )
