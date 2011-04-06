"""

  >>> dolmen.testing.grok(__name__)

We should find the ``cavepainting`` view for a mammoth::

  >>> manfred = Mammoth()
  >>> from zope.interface import implements
  >>> from cromlech.io.tests import TestRequest
  >>> request = TestRequest()
  >>> from zope import component
  >>> view = dolmen.query_view(request, manfred, name='cavepainting')
  >>> print str(view())
  A cave painting of a mammoth

  >>> view.context is manfred
  True
  >>> view.request is request
  True

  >>> from zope.interface.verify import verifyObject
  >>> from cromlech.browser.interfaces import IView
  >>> verifyObject(IView, view)
  True

Look up a view with a name explicitly set with ``dolmen.name``::

  >>> view = dolmen.query_view(request, manfred, name='meal')
  >>> print str(view())
  Mammoth burger

There's no view 'food'::

  >>> view = dolmen.query_view(request, manfred, name='food')
  Traceback (most recent call last):
    ...
  ComponentLookupError: ((<dolmen.view.tests.view.view.Mammoth object at ...>,
            <cromlech.io.tests.TestRequest object at 0x...>),
            <InterfaceClass cromlech.browser.interfaces.IView>,
            'food')

"""

import dolmen.view as dolmen
from cromlech.io.tests import TestResponse


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    responseFactory = TestResponse

    def render(self, *args, **kwargs):
        return 'A cave painting of a mammoth'


class Food(dolmen.View):
    """Grok says: ME NO SEE MAMMOTH, ME SEE MEAL!"""
    dolmen.name('meal')

    responseFactory = TestResponse

    def render(self, *args, **kwargs):
        return 'Mammoth burger'
