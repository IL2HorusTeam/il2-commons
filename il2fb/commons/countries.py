from candv import Constants
from candv import VerboseConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class Country(VerboseConstant):
  ...


@export
class Countries(with_constant_class(Country), Constants):
  au = Country(verbose_name=_("Australia"))
  fi = Country(verbose_name=_("Finland"))
  fr = Country(verbose_name=_("France"))
  de = Country(verbose_name=_("Germany"))
  hu = Country(verbose_name=_("Hungary"))
  jp = Country(verbose_name=_("Japan"))
  it = Country(verbose_name=_("Italy"))
  nl = Country(verbose_name=_("Netherlands"))
  nz = Country(verbose_name=_("New Zealand"))
  pl = Country(verbose_name=_("Poland"))
  ro = Country(verbose_name=_("Romania"))
  sk = Country(verbose_name=_("Slovakia"))
  su = Country(verbose_name=_("Soviet Union"))
  uk = Country(verbose_name=_("United Kingdom"))
  us = Country(verbose_name=_("United States"))
