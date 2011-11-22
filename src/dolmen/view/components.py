# -*- coding: utf-8 -*-

from cromlech.browser import IView, negotiate
from cromlech.io import IRequest
from grokcore.component import baseclass, implements
from zope.component import getMultiAdapter
from zope.location import Location


class View(Location):
    baseclass()
    implements(IView)

    template = None
    response = None
    responseFactory = None  # subclass has to provide one !

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def namespace(self):
        """Returns a dictionary of namespaces that the template
        implementation expects to always be available.
        """
        namespace = {}
        namespace['context'] = self.context
        namespace['request'] = self.request
        namespace['view'] = self
        return namespace

    def update(self, *args, **kwargs):
        self.response = self.responseFactory()

    @property
    def target_language(self):
        return negotiate(self.request)

    def render(self, *args, **kwargs):
        """This is the default render method.
        Not providing a template will make it fails.
        Override this method, if needed (eg: return a string)
        """
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(self, target_language=self.target_language)

    def __call__(self, *args, **kwargs):
        self.update(*args, **kwargs)
        if not self.response.status_int in [301, 302]:
            self.response.write(self.render(*args, **kwargs) or u'')
        return self.response


def query_view(request, context, interface=IView, name=''):
    assert interface.isOrExtends(IView)
    assert IRequest.providedBy(request)
    return getMultiAdapter((context, request), interface, name=name)
