# -*- coding: utf-8 -*-

try:
    import martian
    import grokcore.security
    from dolmen import view
    from cromlech.browser import IRenderable, IResponseFactory

    class ViewSecurityGrokker(martian.ClassGrokker):
        martian.component(view.View)
        martian.directive(grokcore.security.require, name='permission')

        def execute(self, factory, config, permission, **kw):
            for iface in (IRenderable, IResponseFactory):
                for method_name in iface:
                    config.action(
                        discriminator=('protectName', factory, method_name),
                        callable=grokcore.security.util.protect_getattr,
                        args=(factory, method_name, permission))
            return True

except ImportError:
    pass
