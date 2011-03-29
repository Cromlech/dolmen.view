# -*- coding: utf-8 -*-

try:
    import grokcore.security
    from cromlech.io.interfaces import IRenderer
    from grokcore.security.util import check_permission
    from zope.security.checker import NamesChecker, defineChecker

    def make_checker(factory, view_factory, permission, method_names=None):
        if method_names is None:
            method_names = ['__call__']
        if permission is not None:
            check_permission(factory, permission)
        if permission is None or permission == 'zope.Public':
            checker = NamesChecker(method_names)
        else:
            checker = NamesChecker(method_names, permission)
        defineChecker(view_factory, checker)


    class ViewSecurityGrokker(martian.ClassGrokker):
        martian.component(view.View)
        martian.directive(grokcore.security.require, name='permission')

        def execute(self, factory, config, permission, **kw):
            # we can also check here for ISecuredItem
            for method_name in IRenderer:
                config.action(
                    discriminator=('protectName', factory, method_name),
                    callable=grokcore.security.util.protect_getattr,
                    args=(factory, method_name, permission),
                    )
            return True

except ImportError:
    pass
