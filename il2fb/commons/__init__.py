# -*- coding: utf-8 -*-
from candv import (
    SimpleConstant, Constants, Values, ValueConstant, VerboseValueConstant,
)

from il2fb.commons.utils.translation import ugettext_lazy as _


class SupportedLanguages(Constants):
    en = SimpleConstant()
    ru = SimpleConstant()

    @classmethod
    def get_default(cls):
        return cls.en


class GameVersions(Values):
    v4_12 = ValueConstant('4.12')
    v4_12_1 = ValueConstant('4.12.1')
    v4_12_2 = ValueConstant('4.12.2')


class Skills(Values):
    rookie = VerboseValueConstant(0, _("rookie"))
    average = VerboseValueConstant(1, _("average"))
    veteran = VerboseValueConstant(2, _("veteran"))
    ace = VerboseValueConstant(3, _("ace"))
