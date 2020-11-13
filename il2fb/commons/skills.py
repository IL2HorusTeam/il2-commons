from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class SkillConstant(VerboseValueConstant):
  ...


@export
class SKILL(with_constant_class(SkillConstant), Values):
  ROOKIE  = SkillConstant(0, _("rookie"))
  AVERAGE = SkillConstant(1, _("average"))
  VETERAN = SkillConstant(2, _("veteran"))
  ACE     = SkillConstant(3, _("ace"))
