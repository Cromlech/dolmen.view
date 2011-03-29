"""
When a view's update() method redirects somewhere else, the template
is not executed subsequently.

  >>> grok.testing.grok(__name__)

  >>> manfred = Mammoth()

  >>> from webob import Request
  >>> request = Request.blank('/')

  >>> from zope.component import getMultiAdapter
  >>> view = getMultiAdapter((manfred, request), name='cavepainting')
  >>> print view()
  None
  >>> print view.response.getStatus()
  302
  >>> print view.response.headers.get('Location')
  somewhere-else

"""
import grokcore.view as grok

class Mammoth(grok.Context):
    pass

class CavePainting(grok.View):
    def update(self):
        super(CavePainting, self).update()
        self.redirect('somewhere-else')


cavepainting = grok.PageTemplate("""\
<html>
<body>
<h1 tal:content="this-is-an-error" />
</body>
</html>
""")
