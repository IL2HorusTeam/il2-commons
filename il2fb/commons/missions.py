from candv import Constants
from candv import SimpleConstant
from candv import with_constant_class

from ._utils import export


@export
class MissionStatus(SimpleConstant):
  ...


@export
class MissionStatuses(with_constant_class(MissionStatus), Constants):
  not_loaded = MissionStatus()
  loaded     = MissionStatus()
  playing    = MissionStatus()
