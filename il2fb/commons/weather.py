from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import pgettext_lazy as P_

from ._utils import export


@export
class WeatherConditionConstant(VerboseValueConstant):
  ...


@export
class WEATHER_CONDITIONS(with_constant_class(WeatherConditionConstant), Values):
  CLEAR         = WeatherConditionConstant(0, P_("weather", "clear"))
  GOOD          = WeatherConditionConstant(1, P_("weather", "good"))
  HAZY          = WeatherConditionConstant(2, P_("weather", "hazy"))
  POOR          = WeatherConditionConstant(3, P_("weather", "poor"))
  BLIND         = WeatherConditionConstant(4, P_("weather", "blind"))
  PRECIPITATION = WeatherConditionConstant(5, P_("weather", "precipitation"))
  THUNDERSTORM  = WeatherConditionConstant(6, P_("weather", "thunderstorm"))


@export
class WindGustConstant(VerboseValueConstant):
  ...


@export
class WIND_GUSTS(with_constant_class(WindGustConstant), Values):
  NONE     = WindGustConstant(0,  P_("gust", "none"))
  LOW      = WindGustConstant(8,  P_("gust", "low"))
  MODERATE = WindGustConstant(10, P_("gust", "moderate"))
  STRONG   = WindGustConstant(12, P_("gust", "strong"))


@export
class TurbulenceConstant(VerboseValueConstant):
  ...


@export
class TURBULENCES(with_constant_class(TurbulenceConstant), Values):
  NONE        = TurbulenceConstant(0, P_("turbulence", "none"))
  LOW         = TurbulenceConstant(3, P_("turbulence", "low"))
  MODERATE    = TurbulenceConstant(4, P_("turbulence", "moderate"))
  STRONG      = TurbulenceConstant(5, P_("turbulence", "strong"))
  VERY_STRONG = TurbulenceConstant(6, P_("turbulence", "very strong"))
