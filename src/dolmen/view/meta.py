#!/usr/bin/python
# -*- coding: utf-8 -*-

import martian
from dolmen import view
from cromlech.browser import IView
from zope.component import provideAdapter


def default_view_name(factory, module=None, **data):
    return factory.__name__.lower()


class ViewGrokker(martian.ClassGrokker):
    martian.component(view.View)
    martian.directive(view.context)
    martian.directive(view.request)
    martian.directive(view.provides, default=IView)
    martian.directive(view.name, get_default=default_view_name)

    def execute(self, factory, config, context, request, provides, name, **kw):

        factory.__component_name__ = name
        adapts = (context, request)

        config.action(
            discriminator=('adapter', adapts, provides, name),
            callable=provideAdapter,
            args=(factory, adapts, provides, name))

        return True
