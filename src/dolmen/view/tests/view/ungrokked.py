"""
Prove that we can instantiate things from unit tests without grokking.

  >>> view = Ungrokked(None, None)
  
This should not raise an exception, at least.

  >>> view.__name__ is None
  True
  
"""
from dolmen.view import View


class Ungrokked(View):
    pass
