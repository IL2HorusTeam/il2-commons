# -*- coding: utf-8 -*-
from candv import Values, VerboseValueConstant

from il2_commons.utils.translation import ugettext_lazy as _


class Conditions(Values):
    clear = VerboseValueConstant(0, _("clear"))
    good = VerboseValueConstant(1, _("good"))
    hazy = VerboseValueConstant(2, _("hazy"))
    poor = VerboseValueConstant(3, _("poor"))
    blind = VerboseValueConstant(4, _("blind"))
    rain_snow = VerboseValueConstant(5, _("rain or snow"))
    thunderstorm = VerboseValueConstant(6, _("thunderstorm"))


class Gust(Values):
    none = VerboseValueConstant(0, _("none"))
    low = VerboseValueConstant(1, _("low"))
    moderate = VerboseValueConstant(2, _("moderate"))
    strong = VerboseValueConstant(3, _("strong"))


class Turbulence(Values):
    none = VerboseValueConstant(0, _("none"))
    low = VerboseValueConstant(1, _("low"))
    moderate = VerboseValueConstant(2, _("moderate"))
    strong = VerboseValueConstant(3, _("strong"))
    very_strong = VerboseValueConstant(4, _("very strong"))
