from candv import Constants
from candv import SimpleConstant
from candv import with_constant_class

from ._utils import export


@export
class SupportedLanguage(SimpleConstant):
  ...


@export
class SupportedLanguages(with_constant_class(SupportedLanguage), Constants):
  en = SupportedLanguage()
  ru = SupportedLanguage()

  @classmethod
  def get_default(cls):
    return cls.en
