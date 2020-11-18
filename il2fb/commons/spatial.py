from dataclasses import dataclass

from .structures import PrimitiveDataclassMixin

from ._utils import export


@export
@dataclass(frozen=True)
class Point2D(PrimitiveDataclassMixin):
  __slots__ = ["x", "y", ]

  x: float
  y: float


@export
@dataclass(frozen=True)
class Point3D(PrimitiveDataclassMixin):
  __slots__ = ["x", "y", "z", ]

  x: float
  y: float
  z: float
