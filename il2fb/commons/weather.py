from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class WeatherCondition(VerboseValueConstant):
  ...


@export
class WeatherConditions(with_constant_class(WeatherCondition), Values):
  clear         = WeatherCondition(0, _("clear"))
  good          = WeatherCondition(1, _("good"))
  hazy          = WeatherCondition(2, _("hazy"))
  poor          = WeatherCondition(3, _("poor"))
  blind         = WeatherCondition(4, _("blind"))
  precipitation = WeatherCondition(5, _("precipitation"))
  thunderstorm  = WeatherCondition(6, _("thunderstorm"))


@export
class WindGust(VerboseValueConstant):
  ...


@export
class WindGusts(with_constant_class(WindGust), Values):
  none     = WindGust(0,  _("none"))
  low      = WindGust(8,  _("low_gust"))
  moderate = WindGust(10, _("moderate_gust"))
  strong   = WindGust(12, _("strong_gust"))


@export
class TurbulenceType(VerboseValueConstant):
  ...


@export
class Turbulence(with_constant_class(TurbulenceType), Values):
  none        = TurbulenceType(0, _("none"))
  low         = TurbulenceType(3, _("low_turbulence"))
  moderate    = TurbulenceType(4, _("moderate_turbulence"))
  strong      = TurbulenceType(5, _("strong_turbulence"))
  very_strong = TurbulenceType(6, _("very_strong_turbulence"))
