"""

  >>> troll = TrollPainting()
  >>> response = troll()
  >>> response.status, response.headers
  ('200 OK', {})
  >>> print response.body
  The painting is : A nice painting.

"""
import dolmen.view as dolmen
from cromlech.browser.testing import TestResponse


class TrollPainting(dolmen.ViewCanvas):

    responseFactory = TestResponse

    def update(self):
        self.painting = u"A nice painting."

    def render(self):
        return u"The painting is : %s" % self.painting