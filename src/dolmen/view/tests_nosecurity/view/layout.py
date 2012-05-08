"""

  >>> testing.grok(__name__)

We should find the ``index`` view for a mammoth::

  >>> from zope.interface import implements
  >>> from cromlech.browser.testing import TestRequest

  >>> manfred = Mammoth('Manfred')
  >>> request = TestRequest()
  >>> view = dolmen.query_view(request, manfred, name='index')
  >>> assert view is not None

Unfortunately, it's impossible to render it as no layout is yet registered::

  >>> print view()
  Traceback (most recent call last):
  ...
  RuntimeError: Unable to resolve the layout (name: '')
  for <...MammothView...>


We can see here that the name of the queried layout is empty. This is the
default value for the lookup. We can alter that with the `layoutName` attr::

  >>> view.layoutName = 'cave'
  >>> view()
  Traceback (most recent call last):
  ...
  RuntimeError: Unable to resolve the layout (name: 'cave')
  for <...MammothView...>


We can now register the layout as a multi adapter::

  >>> from zope.component import provideAdapter
  >>> from cromlech.browser.testing import IRequest, ILayout
  
  >>> provideAdapter(Cave, (IRequest, Mammoth), ILayout, name='cave')
  >>> provideAdapter(Food, (IRequest, Mammoth), ILayout, name='food')
  >>> provideAdapter(Revealing, (IRequest, Mammoth), ILayout, name='')

The view should now render::

  >>> response = view()
  >>> print response.body
  <div id='painting'>Mammoth: Manfred</div>

We can hot-swap the layouts ::

  >>> view.layoutName = 'food'
  >>> response = view()
  >>> print response.body
  <div id='food'>Mammoth: Manfred</div>

We can see that it's easy to get the view object in the render method::

  >>> view.layoutName = ''
  >>> response = view()
  >>> print response.body
  Layout for <...MammothView...>

"""

import dolmen.view as dolmen
from dolmen.view import testing
from cromlech.browser.testing import TestLayout, TestResponse


class Mammoth(dolmen.Context):

    def __init__(self, name):
        self.name = name


class Cave(TestLayout):

    def __init__(self, request, view):
        pass

    def __call__(self, content, **kwargs):
        return u"<div id='painting'>%s</div>" % content


class Food(TestLayout):

    def __init__(self, request, view):
        pass

    def __call__(self, content, **kwargs):
        return u"<div id='food'>%s</div>" % content
    

class Revealing(TestLayout):

    def __init__(self, request, view):
        pass

    def __call__(self, content, **kwargs):
        return 'Layout for %r' % kwargs.get('view', None)


class MammothView(dolmen.View):
    dolmen.name('index')

    responseFactory = TestResponse
    make_response = dolmen.make_layout_response

    def render(self, *args, **kwargs):
        return 'Mammoth: %s' % self.context.name
