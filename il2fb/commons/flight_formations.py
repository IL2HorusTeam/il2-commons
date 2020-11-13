from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _


class FlightFormation(VerboseValueConstant):
  ...


class FlightFormations(with_constant_class(FlightFormation), Values):
  echelon_right = FlightFormation("F2", _("echelon right"))
  echelon_left  = FlightFormation("F3", _("echelon left"))
  line_abreast  = FlightFormation("F4", _("line abreast"))
  line_asteam   = FlightFormation("F5", _("line asteam"))
  vic           = FlightFormation("F6", _("vic"))
  finger_four   = FlightFormation("F7", _("finger four"))
  diamond       = FlightFormation("F8", _("diamond"))
