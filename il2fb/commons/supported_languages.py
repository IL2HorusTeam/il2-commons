from candv import Constants
from candv import SimpleConstant
from candv import with_constant_class

from ._utils import export


@export
class SupportedLanguageConstant(SimpleConstant):
  ...


@export
class SUPPORTED_LANGUAGES(with_constant_class(SupportedLanguageConstant), Constants):
  EN = SupportedLanguageConstant()
  RU = SupportedLanguageConstant()

  @classmethod
  def get_default(cls):
    return cls.EN
