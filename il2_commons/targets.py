# -*- coding: utf-8 -*-
from candv import Values, VerboseValueConstant

from il2_commons.utils.translation import ugettext_lazy as _


class TargetType(Values):
    destroy = VerboseValueConstant(0, _("destroy"))
    destroy_bridge = VerboseValueConstant(1, _("destroy bridge"))
    destroy_area = VerboseValueConstant(2, _("destroy area"))
    recon = VerboseValueConstant(3, _("recon"))
    escort = VerboseValueConstant(4, _("escort"))
    cover = VerboseValueConstant(5, _("cover"))
    cover_area = VerboseValueConstant(6, _("cover area"))
    cover_bridge = VerboseValueConstant(7, _("cover bridge"))


class TargetPriority(Values):
    primary = VerboseValueConstant(0, _("primary"))
    secondary = VerboseValueConstant(1, _("secondary"))
    hidden = VerboseValueConstant(2, _("hidden"))
