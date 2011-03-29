"""
Before a view is rendered, the update() method is executed. It can be
used e. g. to execute side effects or set up data for use in the
template.

  >>> dolmen.testing.grok(__name__)

  >>> from zope.publisher.browser import TestRequest
  >>> from zope.component import getMultiAdapter

  >>> manfred = Mammoth()
  >>> request = TestRequest()
  >>> view = getMultiAdapter((manfred, request), name='cavepainting')
  >>> print str(view())
  red

"""
import dolmen.view as dolmen


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    def update(self):
        super(CavePainting, self).update()
        self.color = "red"

    def render(self):
        return self.color
