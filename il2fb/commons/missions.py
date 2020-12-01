from candv import Constants
from candv import SimpleConstant
from candv import with_constant_class

from ._utils import export


@export
class MissionStatusConstant(SimpleConstant):
  ...


@export
class MISSION_STATUSES(with_constant_class(MissionStatusConstant), Constants):
  NOT_LOADED = MissionStatusConstant()
  LOADED     = MissionStatusConstant()
  PLAYING    = MissionStatusConstant()
