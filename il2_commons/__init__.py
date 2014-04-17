# -*- coding: utf-8 -*-
from candv import Values, VerboseValueConstant

from il2_commons.utils.translation import ugettext_lazy as _


class Skill(Values):
    rookie = VerboseValueConstant(0, _("rookie"))
    average = VerboseValueConstant(1, _("average"))
    veteran = VerboseValueConstant(2, _("veteran"))
    ace = VerboseValueConstant(3, _("ace"))
