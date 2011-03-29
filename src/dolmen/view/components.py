# -*- coding: utf-8 -*-

import webob
from zope import interface
from zope.location import Location
from cromlech.io import IResponse
from cromlech.browser import interfaces


class Response(webob.Response):
    interface.implements(IResponse)

    charset = 'utf-8'

    def getStatus(self, as_int=True):
        """returns the status of the response
        """
        if not as_int:
            return self.status
        return self.status_int

    def redirect(self, url, status=302, trusted=False):
        """Sets the response for a redirect.
        """
        self.location = url
        self.status = status

    def __str__(self):
        return self.body


class ViewSupport(object):
    """Mixin class providing methods and properties generally
    useful for view-ish components.
    """
    interface.implements(interfaces.IView)
    
    responseFactory = Response

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.response = None

    def update(self, **kwargs):
        self.response = self.responseFactory()

    def render(self, **kwargs):
        pass

    def __call__(self):
        self.update()
        if not self.response.getStatus() in [301, 302]:
            self.response.write(self.render() or u'')
        return self.response

    @property
    def body(self):
        """The text of the request body.
        """
        return self.request.body

    def redirect(self, url, status=302, trusted=False):
        """Redirect to `url`.

        The headers of the :attr:`response` are modified so that the
        calling browser gets a redirect status code. Please note, that
        this method returns before actually sending the response to
        the browser.

        `url` is a string that can contain anything that makes sense
        to a browser. Also relative URIs are allowed.

        `status` is a number representing the HTTP status code sent
        back. If not given or ``None``, ``302`` or ``303`` will be
        sent, depending on the HTTP protocol version in use (HTTP/1.0
        or HTTP/1.1).

        `trusted` is a boolean telling whether we're allowed to
        redirect to 'external' hosts. Normally redirects to other
        hosts than the one the request was sent to are forbidden and
        will raise a :exc:`ValueError`.
        """
        return self.response.redirect(url, status=status, trusted=trusted)


class View(Location, ViewSupport):

    def __init__(self, context, request):
        super(View, self).__init__(context, request)
        self.__name__ = getattr(self, '__view_name__', None)


class TemplateView(View):

    template = None

    def namespace(self):
        """Returns a dictionary of namespaces that the template
        implementation expects to always be available.
        """
        namespace = {}
        namespace['context'] = self.context
        namespace['request'] = self.request
        namespace['static'] = self.static
        namespace['view'] = self
        return namespace

    def render(self, **kwargs):
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(self)
