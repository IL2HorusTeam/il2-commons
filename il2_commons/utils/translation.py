# -*- coding: utf-8 -*-
"""
Translation helpers.
"""
try:
    from django.conf import settings
    if settings.configured:
        from django.utils.translation import (gettext, gettext_lazy,
                                              ugettext, ugettext_lazy, )
    else:
        raise ImportError()
except ImportError:
    from gettext import gettext

    def gettext_lazy(message):
        return gettext(message)

    def ugettext(message):
        return unicode(gettext(message))

    def ugettext_lazy(message):
        return ugettext(message)
