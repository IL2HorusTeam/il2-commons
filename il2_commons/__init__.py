# -*- coding: utf-8 -*-
from candv import Values, ValueConstant, VerboseValueConstant

from il2_commons.utils.translation import ugettext_lazy as _


class GameVersion(Values):
    v4_12 = ValueConstant('4.12')
    v4_12_1 = ValueConstant('4.12.1')
    v4_12_2 = ValueConstant('4.12.2')


class Skill(Values):
    rookie = VerboseValueConstant(0, _("rookie"))
    average = VerboseValueConstant(1, _("average"))
    veteran = VerboseValueConstant(2, _("veteran"))
    ace = VerboseValueConstant(3, _("ace"))
