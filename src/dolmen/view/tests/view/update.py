"""
Before a view is rendered, the update() method is executed. It can be
used e. g. to execute side effects or set up data for use in the
template.

  >>> dolmen.testing.grok(__name__)

  >>> from cromlech.io.testing import TestRequest
  >>> from zope.component import getMultiAdapter

  >>> manfred = Mammoth()
  >>> request = TestRequest()
  >>> view = getMultiAdapter((manfred, request), name='cavepainting')
  >>> print str(view())
  red

"""
import dolmen.view as dolmen
from cromlech.io.testing import TestResponse


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    responseFactory = TestResponse

    def update(self):
        super(CavePainting, self).update()
        self.color = "red"

    def render(self):
        return self.color
