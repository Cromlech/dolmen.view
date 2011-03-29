"""
Templates with ambiguous context cannot be grokked:

  >>> dolmen.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: Multiple possible contexts for
  <class 'dolmen.view.tests.view.ambiguouscontext.Club'>, please use the
  'context' directive.

"""

import dolmen.view as dolmen


class Cave(dolmen.Context):
    pass


class Mammoth(dolmen.Context):
    pass


class Club(dolmen.View):
    pass
