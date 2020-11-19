import dataclasses
import sys

if sys.version_info >= (3, 9):
  Dict = dict
else:
  from typing import Dict

from collections import UserString

from typing import Any
from typing import ClassVar
from typing import Optional

from .typing import String

from ._utils import export


@export
@dataclasses.dataclass(frozen=True)
class VerboseDataclassMixin:
  verbose_name: ClassVar[String] = dataclasses.field(
    init=False,
  )
  help_text: ClassVar[Optional[String]] = dataclasses.field(
    init=False,
    default=None,
  )


@export
class PrimitiveDataclassMixin:

  def to_primitive(self, *args, **kwargs) -> Dict[str, Any]:
    return {
      key: self._value_to_primitive(getattr(self, key), *args, **kwargs)
      for key in self.__dataclass_fields__.keys()
    }

  @staticmethod
  def _value_to_primitive(value: Any, *args, **kwargs) -> Any:
    if value is None:
      return

    if hasattr(value, "to_primitive"):
      return value.to_primitive(*args, **kwargs)

    if hasattr(value, "isoformat"):
      return value.isoformat()

    if isinstance(value, UserString):
      return str(value)

    return value

  @classmethod
  def from_primitive(cls, value: Dict[str, Any], *args, **kwargs) -> Any:
    kwargs = {
      key: cls._value_from_primitive(
        value=value[key],
        type_=field.type,
        *args,
        **kwargs
      )
      for key, field in cls.__dataclass_fields__.items()
      if field.init
    }
    return cls(**kwargs)

  @staticmethod
  def _value_from_primitive(value: Any, type_: type, *args, **kwargs) -> Any:
    if value is None:
      return

    if isinstance(value, type_):
      return value

    if hasattr(type_, "fromisoformat"):
      return type_.fromisoformat(value)

    if hasattr(type_, "from_primitive"):
      return type_.from_primitive(value, *args, **kwargs)

    return type_(value)
