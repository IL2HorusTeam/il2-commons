
from candv import Constants
from candv import Values
from candv import VerboseConstant
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class TargetTypeConstant(VerboseValueConstant):
  ...


@export
class TARGET_TYPES(with_constant_class(TargetTypeConstant), Values):
  DESTROY        = TargetTypeConstant(0, _("destroy"))
  DESTROY_AREA   = TargetTypeConstant(1, _("destroy area"))
  DESTROY_BRIDGE = TargetTypeConstant(2, _("destroy bridge"))
  RECON          = TargetTypeConstant(3, _("recon"))
  ESCORT         = TargetTypeConstant(4, _("escort"))
  COVER          = TargetTypeConstant(5, _("cover"))
  COVER_AREA     = TargetTypeConstant(6, _("cover area"))
  COVER_BRIDGE   = TargetTypeConstant(7, _("cover bridge"))


@export
class TargetPriorityConstant(VerboseValueConstant):
  ...


@export
class TARGET_PRIORITIES(with_constant_class(TargetPriorityConstant), Values):
  PRIMARY   = TargetPriorityConstant(0, _("primary"))
  SECONDARY = TargetPriorityConstant(1, _("secondary"))
  HIDDEN    = TargetPriorityConstant(2, _("hidden"))


@export
class TargetStateConstant(VerboseConstant):
  ...


@export
class TARGET_STATES(with_constant_class(TargetStateConstant), Constants):
  COMPLETE = TargetStateConstant(verbose_name=_("Complete"))
  FAILED   = TargetStateConstant(verbose_name=_("Failed"))
