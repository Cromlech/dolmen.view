"""
When a view's update() method redirects somewhere else, the template
is not executed subsequently.

  >>> dolmen.testing.grok(__name__)

  >>> manfred = Mammoth()

  >>> from cromlech.io.testing import TestRequest
  >>> from zope.interface import implements
  >>> from cromlech.io import IRequest

  >>> request = TestRequest(path='/')

  >>> from dolmen.view.components import query_view
  >>> view = query_view(request, manfred, name='cavepainting')
  >>> view() is view.response
  True
  >>> print view.response.status_int
  302
  >>> print view.response.headers['Location']
  somewhere-else

"""
import dolmen.view as dolmen
from cromlech.webob.response import Response


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    responseFactory = Response

    def update(self):
        super(CavePainting, self).update()
        self.response.redirect("somewhere-else")

    def render(self):
        raise RuntimeError('This is an evil error')
