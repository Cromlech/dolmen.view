"""
Views can also provide an interface, in which case they can be looked up (via
query_view) on the interface. This approach is a bit more explicit than
requiring all views to have a certain name, since this is an interface/contract
rather than an arbitrary naming standard.

First, do some initialization

  >>> dolmen.testing.grok(__name__)
  >>> manfred = Mammoth()
  >>> from cromlech.browser.testing import TestRequest
  >>> request = TestRequest()
  >>> from dolmen.view.components import query_view

If dolmen.name is used, it needs to be supplied. If not supplied, dolmen.name
defaults to the lowercase of the class:

  >>> view = query_view(request, manfred, name='cavepainting')
  >>> print str(view())
  a chalk cave painting

It is also possible to look up the same view by also including the interface::

  >>> view = query_view(request, manfred, interface=IChalk,
  ...                   name='cavepainting')
  >>> print str(view())
  a chalk cave painting

The name can be set to '', in which case it is an 'unnamed' view:

  >>> view = query_view(request, manfred, interface=IRealist)
  >>> print str(view())
  a realist cave painting

Multiple IPaintStyles can now be looked up by interface, rather than name:

  >>> view = query_view(request, manfred, interface=IImpressionist)
  >>> print str(view())
  an impressionist cave painting

"""

import dolmen.view as dolmen
from cromlech.browser.interfaces import IView
from cromlech.browser.testing import TestResponse


class Mammoth(dolmen.Context):
    pass


class IPaintStyle(IView):
    pass


class IChalk(IPaintStyle):
    pass


class IImpressionist(IPaintStyle):
    pass


class IRealist(IPaintStyle):
    pass


class CavePainting(dolmen.View):
    dolmen.provides(IChalk)

    responseFactory = TestResponse

    def render(self):
        return "a chalk cave painting"


class ImpressionistCavePainting(dolmen.View):
    dolmen.provides(IImpressionist)
    dolmen.name('')

    responseFactory = TestResponse

    def render(self):
        return "an impressionist cave painting"


class RealistCavePainting(dolmen.View):
    dolmen.provides(IRealist)
    dolmen.name('')

    responseFactory = TestResponse

    def render(self):
        return "a realist cave painting"
