"""
When a view's update() method redirects somewhere else, the template
is not executed subsequently.

  >>> dolmen.testing.grok(__name__)

  >>> manfred = Mammoth()

  >>> from webob import Request
  >>> request = Request.blank('/')

  >>> from zope.component import getMultiAdapter
  >>> from cromlech.io.interfaces import IRenderer
  
  >>> view = getMultiAdapter((manfred, request), IRenderer, name='cavepainting')
  >>> print view()
  None
  >>> print view.response.getStatus()
  302
  >>> print view.response.headers.get('Location')
  somewhere-else

"""
import dolmen.view as dolmen


class Mammoth(dolmen.Context):
    pass


class CavePainting(dolmen.View):

    def update(self):
        super(CavePainting, self).update()
        self.response.redirect("somewhere-else")

    def render(self):
        raise RuntimeError('This is an evil error')
