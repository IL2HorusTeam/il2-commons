from candv import Constants
from candv import VerboseConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class CountryConstant(VerboseConstant):
  ...


@export
class COUNTRY(with_constant_class(CountryConstant), Constants):
  AU = CountryConstant(verbose_name=_("Australia"))
  FI = CountryConstant(verbose_name=_("Finland"))
  FR = CountryConstant(verbose_name=_("France"))
  DE = CountryConstant(verbose_name=_("Germany"))
  HU = CountryConstant(verbose_name=_("Hungary"))
  JP = CountryConstant(verbose_name=_("Japan"))
  IT = CountryConstant(verbose_name=_("Italy"))
  NL = CountryConstant(verbose_name=_("Netherlands"))
  NZ = CountryConstant(verbose_name=_("New Zealand"))
  PL = CountryConstant(verbose_name=_("Poland"))
  RO = CountryConstant(verbose_name=_("Romania"))
  SK = CountryConstant(verbose_name=_("Slovakia"))
  SU = CountryConstant(verbose_name=_("Soviet Union"))
  UK = CountryConstant(verbose_name=_("United Kingdom"))
  US = CountryConstant(verbose_name=_("United States"))
