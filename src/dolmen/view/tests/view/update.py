"""
Before a view is rendered, the update() method is executed. It can be
used e. g. to execute side effects or set up data for use in the
template.

  >>> grok.testing.grok(__name__)

  >>> from zope.publisher.browser import TestRequest
  >>> from zope.component import getMultiAdapter

  >>> manfred = Mammoth()
  >>> request = TestRequest()
  >>> view = getMultiAdapter((manfred, request), name='cavepainting')
  >>> print str(view())
  <html>
  <body>
  <h1>red</h1>
  <h1>red</h1>
  </body>
  </html>


"""
import grokcore.view as grok


class Mammoth(grok.Context):
    pass


class CavePainting(grok.View):
    def update(self):
        super(CavePainting, self).update()
        self.color = "red"


cavepainting = grok.PageTemplate("""\
<html>
<body>
<h1 tal:content="view/color"/>
<h1 tal:content="python: view.color"/>
</body>
</html>
""")
