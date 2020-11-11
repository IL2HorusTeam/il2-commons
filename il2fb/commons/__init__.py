from candv import Constants
from candv import SimpleConstant
from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from .translations import gettext_lazy as _


class SupportedLanguage(SimpleConstant):
  ...


class SupportedLanguages(with_constant_class(SupportedLanguage), Constants):
  en = SupportedLanguage()
  ru = SupportedLanguage()

  @classmethod
  def get_default(cls):
    return cls.en


class Skill(VerboseValueConstant):
  ...


class Skills(with_constant_class(Skill), Values):
  rookie  = Skill(0, _("rookie"))
  average = Skill(1, _("average"))
  veteran = Skill(2, _("veteran"))
  ace     = Skill(3, _("ace"))


class UnitType(VerboseValueConstant):
  ...


class UnitTypes(with_constant_class(UnitType), Values):
  aircraft   = UnitType('planes',      _("aircraft"))
  armor      = UnitType('armor',       _("armor"))
  artillery  = UnitType('artillery',   _("artillery"))
  balloon    = UnitType('aeronautics', _("balloon"))
  light      = UnitType('lights',      _("light"))
  radio      = UnitType('radios',      _("radio"))
  ship       = UnitType('ships',       _("ship"))
  stationary = UnitType('stationary',  _("stationary"))
  train      = UnitType('trains',      _("train"))
  vehicle    = UnitType('vehicles',    _("vehicle"))


class MissionStatus(SimpleConstant):
  ...


class MissionStatuses(with_constant_class(MissionStatus), Constants):
  not_loaded = MissionStatus()
  loaded     = MissionStatus()
  playing    = MissionStatus()
