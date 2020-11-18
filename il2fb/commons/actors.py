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
class Human(Actor):
  __slots__ = ["callsign", ]

  callsign: str


@export
@dataclass(frozen=True)
class HumanAircraft(Human):
  __slots__ = Human.__slots__ + ["aircraft", ]

  aircraft: str


@export
@dataclass(frozen=True)
class HumanAircraftCrewMember(HumanAircraft):
  __slots__ = HumanAircraft.__slots__ + ["index", ]

  index: int


@export
@dataclass(frozen=True)
class AIAircraft(Actor):
  __slots__ = ["flight_id", "aircraft", ]

  flight_id: str
  aircraft:  str


@export
@dataclass(frozen=True)
class AIAircraftCrewMember(AIAircraft):
  __slots__ = AIAircraft.__slots__ + ["index", ]

  index: int


@export
@dataclass(frozen=True)
class Unit(Actor):
  __slots__ = ["id", ]

  id: str


@export
@dataclass(frozen=True)
class StationaryUnit(Unit):
  ...


@export
@dataclass(frozen=True)
class MovingUnit(Unit):
  ...


@export
@dataclass(frozen=True)
class MovingUnitMember(MovingUnit):
  __slots__ = MovingUnit.__slots__ + ["index", ]

  index: int


@export
@dataclass(frozen=True)
class Building(Actor):
  __slots__ = ["name", ]

  name: str


@export
@dataclass(frozen=True)
class Bridge(Actor):
  __slots__ = ["id", ]

  id: str
