# -*- coding: utf-8 -*-
from candv import Values, VerboseValueConstant

from il2_commons.utils.translation import ugettext_lazy as _


class Formation(Values):
    echelon_right = VerboseValueConstant('F1', _("echelon right"))
    echelon_left = VerboseValueConstant('F2', _("echelon left"))
    rank = VerboseValueConstant('F3', _("rank"))
    line_abreast = VerboseValueConstant('F4', _("line abreast"))
    line_asteam = VerboseValueConstant('F5', _("line asteam"))
    vic = VerboseValueConstant('F6', _("vic"))
    finger_four = VerboseValueConstant('F7', _("finger four"))
    diamond = VerboseValueConstant('F8', _("diamond"))
