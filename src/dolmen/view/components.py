# -*- coding: utf-8 -*-

from zope import interface
from zope.location import Location
from cromlech.io import IResponse
from dolmen.view import interfaces
from grokcore.component import baseclass


class View(Location):
    baseclass()

    template = None
    responseFactory = None

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.response = None

    def namespace(self):
        """Returns a dictionary of namespaces that the template
        implementation expects to always be available.
        """
        namespace = {}
        namespace['context'] = self.context
        namespace['request'] = self.request
        namespace['view'] = self
        return namespace

   def update(self, **kwargs):
        self.response = self.responseFactory()

    def render(self, **kwargs):
        """This is the default render method.
        Not providing a template will make it fails.
        Override this method, if needed (eg: return a string)
        """
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(self)

    def __call__(self):
        self.update()
        if not self.response.getStatus() in [301, 302]:
            self.response.write(self.render() or u'')
        return self.response
