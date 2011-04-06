"""
When a view's update() method redirects somewhere else, the template
is not executed subsequently.

  >>> dolmen.testing.grok(__name__)

  >>> manfred = Mammoth()

  >>> from webob import Request
  >>> from zope.interface import implements
  >>> from cromlech.io import IRequest
  >>> class TestRequest(Request):
  ...     implements(IRequest)
  >>> request = TestRequest.blank('/')

  >>> from dolmen.view.components import query_view
  >>> view = query_view(request, manfred, name='cavepainting')
  >>> view() is view.response
  True
  >>> print view.response.getStatus()
  302
  >>> print view.response.headers.get('Location')
  somewhere-else

"""
import dolmen.view as dolmen
from cromlech.io.tests import TestResponse


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    responseFactory = TestResponse

    def update(self):
        super(CavePainting, self).update()
        self.response.redirect("somewhere-else")

    def render(self):
        raise RuntimeError('This is an evil error')
