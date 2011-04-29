"""
Views without a context cannot be grokked:

  >>> dolmen.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: No module-level context for
  <class 'dolmen.view.tests_nosecurity.view.missingcontext.Club'>, please use the
  'context' directive.

"""

import dolmen.view as dolmen


class Club(dolmen.View):
    pass
