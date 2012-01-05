# -*- coding: utf-8 -*-

from cromlech.browser import IView, ILayout, ITemplate
from cromlech.browser.exceptions import HTTPRedirect
from cromlech.browser.utils import redirect_exception_response
from cromlech.i18n import ILanguage
from cromlech.io import IRequest
from grokcore.component import baseclass, implements
from zope.component import getMultiAdapter
from zope.location import Location


def query_view(request, context, interface=IView, name=''):
    assert interface.isOrExtends(IView)
    assert IRequest.providedBy(request)
    return getMultiAdapter((context, request), interface, name=name)


def query_view_template(view):
    """Returns a template associated to a view, or None.
    """
    return queryMultiAdapter((view, view.request), ITemplate)


def query_view_layout(request, view, name=""):
    """Returns a layout associated to the view's request and context.
    """
    return queryMultiAdapter((view.request, view.context), ILayout, name=name)


def layout_renderer(name=""):
    """Factory allowing to generate a view method able to embed a view's
    rendering inside the layout with the given name.
    """
    def view_layout_call(view, *args, **kwargs):
        """This is a view method-like function that allows the view to
        rendering itself in a layout. It can be used as a view __call__
        replacer.
        """
        try:
            view.update(*args, **kwargs)
            layout = query_view_layout(view.request, view, name)
            return layout(view.render(*args, **kwargs), view=view)
        except HTTPRedirect, exc:
            return redirect_exception_response(view.responseFactory, exc)
    return view_layout_call


class View(Location):
    """A View implements `IView` that is an extended version of a simple
    IHTTPRenderer. It's articulated around 3 methods :
    `update`, `render` and `__call__`.
    """
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
        """Update is called prior to any rendering. This method is left
        empty on purpose, so it can be overriden easily.
        """
        pass

    @property
    def target_language(self):
        """Returns the prefered language by adapting the request.
        If no adapter thus no language is found, None is returned.
        None will, most of the time, mean 'no translation'.
        """
        return ILanguage(self.request, None)

    def render(self, *args, **kwargs):
        """This is the default render method.
        Not providing a template will make it fails.
        Override this method, if needed (eg: return a string)
        """
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(self, target_language=self.target_language)

    def __call__(self, *args, **kwargs):
        """The __call__ method of the view is the glue between the update,
        the rendering and the response.
        """
        try:
            self.update(*args, **kwargs)
            result = self.render(*args, **kwargs)
            self.response = self.responseFactory()
            self.response.write(result or u'')
            return self.response
        except HTTPRedirect, exc:
            return redirect_exception_response(self.responseFactory, exc)
