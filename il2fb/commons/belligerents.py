from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class Belligerent(VerboseValueConstant):
  ...


@export
class Belligerents(with_constant_class(Belligerent), Values):
  none      = Belligerent(0,  _("none"))
  red       = Belligerent(1,  _("red"))
  blue      = Belligerent(2,  _("blue"))
  green     = Belligerent(3,  _("green"))
  gold      = Belligerent(4,  _("gold"))
  purple    = Belligerent(5,  _("purple"))
  aqua      = Belligerent(6,  _("aqua"))
  maroon    = Belligerent(7,  _("maroon"))
  navy      = Belligerent(8,  _("navy"))
  emerald   = Belligerent(9,  _("emerald"))
  olive     = Belligerent(10, _("olive"))
  magenta   = Belligerent(11, _("magenta"))
  teal      = Belligerent(12, _("teal"))
  orange    = Belligerent(13, _("orange"))
  turquoise = Belligerent(14, _("turquoise"))
  brown     = Belligerent(15, _("brown"))
  salad     = Belligerent(16, _("salad"))
