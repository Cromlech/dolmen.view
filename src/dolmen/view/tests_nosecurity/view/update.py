"""
Before a view is rendered, the update() method is executed. It can be
used e. g. to execute side effects or set up data for use in the
template.

  >>> from dolmen.view import testing
  >>> testing.grok(__name__)

  >>> from cromlech.browser.testing import TestRequest
  >>> manfred = Mammoth()
  >>> request = TestRequest()

  >>> from zope.component import getMultiAdapter
  >>> view = getMultiAdapter((manfred, request), name='cavepainting')
  >>> print str(view())
  red

"""
import dolmen.view as dolmen
from cromlech.browser.testing import TestResponse


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    responseFactory = TestResponse

    def update(self):
        self.color = "red"

    def render(self):
        return self.color
