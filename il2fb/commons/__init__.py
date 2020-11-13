from .skills import *
from .supported_languages import *
from .units import *

from candv import Constants
from candv import SimpleConstant
from candv import with_constant_class


class MissionStatus(SimpleConstant):
  ...


class MissionStatuses(with_constant_class(MissionStatus), Constants):
  not_loaded = MissionStatus()
  loaded     = MissionStatus()
  playing    = MissionStatus()
