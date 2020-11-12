from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _


class ConditionType(VerboseValueConstant):
  ...


class Conditions(with_constant_class(ConditionType), Values):
  clear         = ConditionType(0, _("clear"))
  good          = ConditionType(1, _("good"))
  hazy          = ConditionType(2, _("hazy"))
  poor          = ConditionType(3, _("poor"))
  blind         = ConditionType(4, _("blind"))
  precipitation = ConditionType(5, _("precipitation"))
  thunderstorm  = ConditionType(6, _("thunderstorm"))


class GustType(VerboseValueConstant):
  ...


class Gust(with_constant_class(GustType), Values):
  none     = GustType(0,  _("none"))
  low      = GustType(8,  _("low_gust"))
  moderate = GustType(10, _("moderate_gust"))
  strong   = GustType(12, _("strong_gust"))


class TurbulenceType(VerboseValueConstant):
  ...


class Turbulence(with_constant_class(TurbulenceType), Values):
  none        = TurbulenceType(0, _("none"))
  low         = TurbulenceType(3, _("low_turbulence"))
  moderate    = TurbulenceType(4, _("moderate_turbulence"))
  strong      = TurbulenceType(5, _("strong_turbulence"))
  very_strong = TurbulenceType(6, _("very_strong_turbulence"))
