from typing import Optional

from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from .typing import String

from ._translations import gettext_lazy as _
from ._utils import export


@export
class BelligerentConstant(VerboseValueConstant):

  def __init__(
    self,
    value:        int,
    color:        str,
    verbose_name: Optional[String] = None,
    help_text:    Optional[String] = None,
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

  def to_primitive(self, *args, **kwargs):
    primitive = super().to_primitive(*args, **kwargs)
    primitive['color'] = self.color
    return primitive


@export
class BELLIGERENT(with_constant_class(BelligerentConstant), Values):
  """
  Definitions of belligerents (a.k.a "armies").

  Extracted from "com.maddox.il2.ai.Army" with colors decoded.

  """
  NONE      = BelligerentConstant(value=0,  color="FFFFFF", verbose_name=_("none"))
  RED       = BelligerentConstant(value=1,  color="C00000", verbose_name=_("red"))
  BLUE      = BelligerentConstant(value=2,  color="0000C0", verbose_name=_("blue"))
  GREEN     = BelligerentConstant(value=3,  color="00C000", verbose_name=_("green"))
  GOLD      = BelligerentConstant(value=4,  color="C0C000", verbose_name=_("gold"))
  PURPLE    = BelligerentConstant(value=5,  color="C000C0", verbose_name=_("purple"))
  AQUA      = BelligerentConstant(value=6,  color="00C0C0", verbose_name=_("aqua"))
  MAROON    = BelligerentConstant(value=7,  color="800000", verbose_name=_("maroon"))
  NAVY      = BelligerentConstant(value=8,  color="000080", verbose_name=_("navy"))
  EMERALD   = BelligerentConstant(value=9,  color="004000", verbose_name=_("emerald"))
  OLIVE     = BelligerentConstant(value=10, color="59800C", verbose_name=_("olive"))
  MAGENTA   = BelligerentConstant(value=11, color="800080", verbose_name=_("magenta"))
  TEAL      = BelligerentConstant(value=12, color="008080", verbose_name=_("teal"))
  ORANGE    = BelligerentConstant(value=13, color="E7651A", verbose_name=_("orange"))
  TURQUOISE = BelligerentConstant(value=14, color="00A49E", verbose_name=_("turquoise"))
  BROWN     = BelligerentConstant(value=15, color="8C6636", verbose_name=_("brown"))
  SALAD     = BelligerentConstant(value=16, color="408040", verbose_name=_("salad"))
