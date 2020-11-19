"""
Primitive actor data structures.

"""
from dataclasses import dataclass

from .structures import PrimitiveDataclassMixin

from ._utils import export


@export
@dataclass(frozen=True)
class Actor(PrimitiveDataclassMixin):
  ...


@export
@dataclass(frozen=True)
class HumanActor(Actor):
  __slots__ = ["callsign", ]

  callsign: str


@export
@dataclass(frozen=True)
class HumanAircraftActor(HumanActor):
  __slots__ = HumanActor.__slots__ + ["aircraft", ]

  aircraft: str


@export
@dataclass(frozen=True)
class HumanAircraftCrewMemberActor(HumanAircraftActor):
  __slots__ = HumanAircraftActor.__slots__ + ["index", ]

  index: int


@export
@dataclass(frozen=True)
class AIAircraftActor(Actor):
  __slots__ = ["flight_id", "aircraft", ]

  flight_id: str
  aircraft:  str


@export
@dataclass(frozen=True)
class AIAircraftCrewMemberActor(AIAircraftActor):
  __slots__ = AIAircraftActor.__slots__ + ["index", ]

  index: int


@export
@dataclass(frozen=True)
class UnitActor(Actor):
  __slots__ = ["id", ]

  id: str


@export
@dataclass(frozen=True)
class StationaryUnitActor(UnitActor):
  ...


@export
@dataclass(frozen=True)
class MovingUnitActor(UnitActor):
  ...


@export
@dataclass(frozen=True)
class MovingUnitMemberActor(MovingUnitActor):
  __slots__ = MovingUnitActor.__slots__ + ["index", ]

  index: int


@export
@dataclass(frozen=True)
class BuildingActor(Actor):
  __slots__ = ["name", ]

  name: str


@export
@dataclass(frozen=True)
class BridgeActor(Actor):
  __slots__ = ["id", ]

  id: str
