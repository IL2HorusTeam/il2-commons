from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class WeatherConditionConstant(VerboseValueConstant):
  ...


@export
class WEATHER_CONDITION(with_constant_class(WeatherConditionConstant), Values):
  CLEAR         = WeatherConditionConstant(0, _("clear"))
  GOOD          = WeatherConditionConstant(1, _("good"))
  HAZY          = WeatherConditionConstant(2, _("hazy"))
  POOR          = WeatherConditionConstant(3, _("poor"))
  BLIND         = WeatherConditionConstant(4, _("blind"))
  PRECIPITATION = WeatherConditionConstant(5, _("precipitation"))
  THUNDERSTORM  = WeatherConditionConstant(6, _("thunderstorm"))


@export
class WindGustConstant(VerboseValueConstant):
  ...


@export
class WIND_GUST(with_constant_class(WindGustConstant), Values):
  NONE     = WindGustConstant(0,  _("none"))
  LOW      = WindGustConstant(8,  _("low_gust"))
  MODERATE = WindGustConstant(10, _("moderate_gust"))
  STRONG   = WindGustConstant(12, _("strong_gust"))


@export
class TurbulenceConstant(VerboseValueConstant):
  ...


@export
class TURBULENCE(with_constant_class(TurbulenceConstant), Values):
  NONE        = TurbulenceConstant(0, _("none"))
  LOW         = TurbulenceConstant(3, _("low_turbulence"))
  MODERATE    = TurbulenceConstant(4, _("moderate_turbulence"))
  STRONG      = TurbulenceConstant(5, _("strong_turbulence"))
  VERY_STRONG = TurbulenceConstant(6, _("very_strong_turbulence"))
