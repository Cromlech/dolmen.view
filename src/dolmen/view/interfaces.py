# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute


class IBaseClasses(Interface):
    View = Attribute("Base class for browser views.")


class IDirectives(Interface):

    def request(interface):
        """Define on which request a component is registered.
        This can be used to narrow to a skin type.
        """

    def view(view):
        """Define on which view a viewlet manager/viewlet is registered.
        """


class IView(Interface):
    """Grok views all provide this interface."""

    context = Attribute('context', "Object that the view presents.")

    request = Attribute('request', "Request that the view was looked up with.")

    static = Attribute('static', "Directory resource containing "
                       "the static files of the view's package.")

    def redirect(url):
        """Redirect to given URL"""

    def namespace():
        """Returns a dictionary that is injected in the template
        namespace.
        """

    def __call__():
        """Returns a full Response object.
        """

    def update():
        """
        """

    def render():
        """
        """


class ISecuredItem(Interface):
    """
    """
