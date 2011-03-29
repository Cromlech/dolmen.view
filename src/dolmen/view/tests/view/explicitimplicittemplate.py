"""
It is too confusing to have a template that would be implicitly
associated with a view while that view already refers to another
template using grok.template.  Therefore there is an error:

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  ConfigurationExecutionError: martian.error.GrokError: Multiple possible templates for view
  <class 'grokcore.view.tests.view.explicitimplicittemplate.Painting'>.
  It uses grok.template('cavepainting'), but there is also a template
  called 'painting'.
  in:
  
"""
import grokcore.view as grok

class Mammoth(grok.Context):
    pass

class Painting(grok.View):
    grok.template('cavepainting')

cavepainting = grok.PageTemplate("GROK CAVEPAINT MAMMOTH!")
painting = grok.PageTemplate("GROK PAINT MAMMOTH!")
