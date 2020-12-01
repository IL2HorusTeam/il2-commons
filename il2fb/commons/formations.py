from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class FlightFormationConstant(VerboseValueConstant):
  ...


@export
class FLIGHT_FORMATIONS(with_constant_class(FlightFormationConstant), Values):
  ECHELON_RIGHT = FlightFormationConstant("F2", _("echelon right"))
  ECHELON_LEFT  = FlightFormationConstant("F3", _("echelon left"))
  LINE_ABREAST  = FlightFormationConstant("F4", _("line abreast"))
  LINE_ASTEAM   = FlightFormationConstant("F5", _("line asteam"))
  VIC           = FlightFormationConstant("F6", _("vic"))
  FINGER_FOUR   = FlightFormationConstant("F7", _("finger four"))
  DIAMOND       = FlightFormationConstant("F8", _("diamond"))
