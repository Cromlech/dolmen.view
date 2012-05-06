"""
When a view's update() method redirects somewhere else, the template
is not executed subsequently.

  >>> from dolmen.view import testing
  >>> testing.grok(__name__)

  >>> manfred = Mammoth()

  >>> from cromlech.browser.testing import TestRequest
  >>> from zope.interface import implements
  >>> from cromlech.io import IRequest

  >>> request = TestRequest(path='/')

  >>> from dolmen.view.components import query_view
  >>> view = query_view(request, manfred, name='cavepainting')
  >>> response = view()
  >>> response.status, response.headers
  ('307 Temporary Redirect', {'Content-Length': '0',
                              'Content-Type': 'text/plain',
                              'Location': 'http://localhost/my_script'})

"""
import dolmen.view as dolmen
from cromlech.browser.testing import TestResponse
from cromlech.browser.exceptions import HTTPTemporaryRedirect


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    responseFactory = TestResponse

    def update(self):
        raise HTTPTemporaryRedirect('http://localhost/my_script')

    def render(self):
        raise RuntimeError('This is an evil error')
