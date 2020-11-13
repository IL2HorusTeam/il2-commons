from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class UnitType(VerboseValueConstant):
  ...


@export
class UnitTypes(with_constant_class(UnitType), Values):
  aircraft   = UnitType("planes",      _("aircraft"))
  armor      = UnitType("armor",       _("armor"))
  artillery  = UnitType("artillery",   _("artillery"))
  balloon    = UnitType("aeronautics", _("balloon"))
  light      = UnitType("lights",      _("light"))
  radio      = UnitType("radios",      _("radio"))
  ship       = UnitType("ships",       _("ship"))
  stationary = UnitType("stationary",  _("stationary"))
  train      = UnitType("trains",      _("train"))
  vehicle    = UnitType("vehicles",    _("vehicle"))
