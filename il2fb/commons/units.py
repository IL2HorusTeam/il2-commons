from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class UnitTypeConstant(VerboseValueConstant):
  ...


@export
class UNIT_TYPE(with_constant_class(UnitTypeConstant), Values):
  AIRCRAFT   = UnitTypeConstant("planes",      _("aircraft"))
  ARMOR      = UnitTypeConstant("armor",       _("armor"))
  ARTILLERY  = UnitTypeConstant("artillery",   _("artillery"))
  BALLOON    = UnitTypeConstant("aeronautics", _("balloon"))
  LIGHT      = UnitTypeConstant("lights",      _("light"))
  RADIO      = UnitTypeConstant("radios",      _("radio"))
  SHIP       = UnitTypeConstant("ships",       _("ship"))
  STATIONARY = UnitTypeConstant("stationary",  _("stationary"))
  TRAIN      = UnitTypeConstant("trains",      _("train"))
  VEHICLE    = UnitTypeConstant("vehicles",    _("vehicle"))
