from typing import Optional

from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class Belligerent(VerboseValueConstant):

  def __init__(
    self,
    value:        int,
    color:        str,
    verbose_name: Optional[str]=None,
    help_text:    Optional[str]=None,
  ):
    super().__init__(
      value=value,
      verbose_name=verbose_name,
      help_text=help_text,
    )
    self.color = color

  def merge_into_group(self, group):
    super().merge_into_group(group)
    group.color = self.color

  def to_primitive(self, context=None):
    primitive = super().to_primitive(context)
    primitive['color'] = self.color
    return primitive


@export
class Belligerents(with_constant_class(Belligerent), Values):
  """
  Definitions of belligerents (a.k.a "armies").

  Extracted from "com.maddox.il2.ai.Army" with colors decoded.

  """
  none      = Belligerent(value=0,  color="FFFFFF", verbose_name=_("none"))
  red       = Belligerent(value=1,  color="C00000", verbose_name=_("red"))
  blue      = Belligerent(value=2,  color="0000C0", verbose_name=_("blue"))
  green     = Belligerent(value=3,  color="00C000", verbose_name=_("green"))
  gold      = Belligerent(value=4,  color="C0C000", verbose_name=_("gold"))
  purple    = Belligerent(value=5,  color="C000C0", verbose_name=_("purple"))
  aqua      = Belligerent(value=6,  color="00C0C0", verbose_name=_("aqua"))
  maroon    = Belligerent(value=7,  color="800000", verbose_name=_("maroon"))
  navy      = Belligerent(value=8,  color="000080", verbose_name=_("navy"))
  emerald   = Belligerent(value=9,  color="004000", verbose_name=_("emerald"))
  olive     = Belligerent(value=10, color="59800C", verbose_name=_("olive"))
  magenta   = Belligerent(value=11, color="800080", verbose_name=_("magenta"))
  teal      = Belligerent(value=12, color="008080", verbose_name=_("teal"))
  orange    = Belligerent(value=13, color="E7651A", verbose_name=_("orange"))
  turquoise = Belligerent(value=14, color="00A49E", verbose_name=_("turquoise"))
  brown     = Belligerent(value=15, color="8C6636", verbose_name=_("brown"))
  salad     = Belligerent(value=16, color="408040", verbose_name=_("salad"))
