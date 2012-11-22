# -*- coding: utf-8 -*-

from cromlech.browser import IRequest, ILayout, ITemplate
from cromlech.browser import IResponseFactory, IRenderable, IView
from cromlech.browser.exceptions import HTTPRedirect
from cromlech.browser.utils import redirect_exception_response
from cromlech.i18n import ILanguage
from zope.location import Location
from zope.interface import implements
from zope.interface.interfaces import ComponentLookupError


def query_view(request, context, interface=IView, name=''):
    assert interface.isOrExtends(IView)
    assert IRequest.providedBy(request)
    return interface(context, request, name=name)


def query_view_template(view, interface=ITemplate, name=""):
    """Returns a template associated to a view, or None.
    """
    assert IView.providedBy(view)
    assert interface.isOrExtends(ITemplate)
    return interface(view, view.request, name=name)


def query_view_layout(view, interface=ILayout, name=""):
    """Returns a layout associated to the view's request and context.
    """
    assert IView.providedBy(view)
    assert interface.isOrExtends(ILayout)
    return interface(view.request, view.context, name=name)


def make_view_response(view, result, *args, **kwargs):
    response = view.responseFactory()
    response.write(result or u'')
    return response


def make_layout_response(view, result, name=None):
    if name is None:
        name = getattr(view, 'layoutName', "")
    layout = query_view_layout(view, name=name)
    if layout is not None:
        wrapped = layout(result, **{'view': view})
        response = view.responseFactory()
        response.write(wrapped or u'')
        return response
    raise RuntimeError(
        'Unable to resolve the layout (name: %r) for %r' % (name, view))


class ViewCanvas(Location):
    """A ViewCanvas implements `IView` that is an extended version
    of a simple IHTTPRenderer. It's articulated around 3 methods :
    `update`, `render` and `__call__`.
    """
    implements(IView, IRenderable, IResponseFactory)

    template = None
    make_response = make_view_response

    target_language = None  # subclass to override or use `update`.
    responseFactory = None  # subclass has to provide one.

    def namespace(self):
        """Returns a dictionary of namespaces that the template
        implementation expects to always be available.
        """
        return {'view': self}

    def update(self):
        """Update is called prior to any rendering. This method is left
        empty on purpose, so it can be overriden easily.
        """
        pass

    def render(self):
        """This is the default render method.
        Not providing a template will make it fails.
        Override this method, if needed (eg: return a string)
        """
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(
            self, target_language=self.target_language, **self.namespace())

    def __call__(self):
        """The __call__ method of the view is the glue between the update,
        the rendering and the response.
        """
        try:
            self.update()
            result = self.render()
            return self.make_response(result)
        except HTTPRedirect, exc:
            return redirect_exception_response(self.responseFactory, exc)


class View(ViewCanvas):
    """A ModelView is a component bound to a model and a request.
    It is meant to be used in an MVC-based application.
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def namespace(self):
        return {
            'view': self,
            'context': self.context,
            'request': self.request,
            }

    @property
    def target_language(self):
        """Returns the prefered language by adapting the request.
        If no adapter thus no language is found, None is returned.
        None will, most of the time, mean 'no translation'.
        """
        try:
            return ILanguage(self.request)
        except ComponentLookupError:
            return None
