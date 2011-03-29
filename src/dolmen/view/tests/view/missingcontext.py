"""
Views without a context cannot be grokked:

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: No module-level context for
  <class 'dolmen.view.tests.view.missingcontext.Club'>, please use the
  'context' directive.

"""

from dolmen.view import View


class Club(View):
    pass
