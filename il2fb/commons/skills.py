from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class Skill(VerboseValueConstant):
  ...


@export
class Skills(with_constant_class(Skill), Values):
  rookie  = Skill(0, _("rookie"))
  average = Skill(1, _("average"))
  veteran = Skill(2, _("veteran"))
  ace     = Skill(3, _("ace"))
