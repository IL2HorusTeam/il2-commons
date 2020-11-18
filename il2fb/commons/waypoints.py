from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class FlightWaypointTypeConstant(VerboseValueConstant):
  ...


@export
class FLIGHT_WAYPOINT_TYPE(with_constant_class(FlightWaypointTypeConstant), Values):

  # Take-off ----------------------------------------------------------------
  TAKEOFF_NORMAL = FlightWaypointTypeConstant(
    "TAKEOFF",
    _("takeoff (normal)"),
  )
  TAKEOFF_PAIR = FlightWaypointTypeConstant(
    "TAKEOFF_002",
    _("takeoff (pair)"),
    )
  TAKEOFF_IN_LINE = FlightWaypointTypeConstant(
    "TAKEOFF_003",
    _("takeoff (in line)"),
  )
  TAKEOFF_TAXIING = FlightWaypointTypeConstant(
    "TAKEOFF_004",
    _("takeoff (taxiing)"),
  )
  TAKEOFF_TAXIING_FROM_STATIC = FlightWaypointTypeConstant(
    "TAKEOFF_005",
    _("takeoff (taxiing from static)"),
  )

  # Normal flight -----------------------------------------------------------
  NORMAL = FlightWaypointTypeConstant(
    "NORMFLY",
    _("normal"),
  )

  # Attack ------------------------------------------------------------------
  AIR_ATTACK = FlightWaypointTypeConstant(
    "X_AIR_ATTACK",
    _("air attack"),
  )
  """
  .. warning::

    "Air attack" is not present in the game. It is calculated as ``NORMFLY``
    with a target.

  """

  GROUND_ATTACK = FlightWaypointTypeConstant(
    "GATTACK",
    _("ground attack"),
  )

  # Patrol ------------------------------------------------------------------
  PATROL_TRIANGLE = FlightWaypointTypeConstant(
    "NORMFLY_401",
    _("patrol (triangle)"),
  )
  PATROL_SQUARE = FlightWaypointTypeConstant(
    "NORMFLY_402",
    _("patrol (square)"),
  )
  PATROL_PENTAGON = FlightWaypointTypeConstant(
    "NORMFLY_403",
    _("patrol (pentagon)"),
  )
  PATROL_HEXAGON = FlightWaypointTypeConstant(
    "NORMFLY_404",
    _("patrol (hexagon)"),
  )
  PATROL_RANDOM = FlightWaypointTypeConstant(
    "NORMFLY_405",
    _("patrol (random)"),
  )

  # Artillery spotter -------------------------------------------------------
  ARTILLERY_SPOTTER = FlightWaypointTypeConstant(
    "NORMFLY_407",
    _("artillery spotter"),
  )

  # Langing -----------------------------------------------------------------
  LANDING_ON_LEFT = FlightWaypointTypeConstant(
    "LANDING",
    _("landing (on left)"),
  )
  LANDING_ON_RIGHT = FlightWaypointTypeConstant(
    "LANDING_101",
    _("landing (on right)"),
  )
  LANDING_SHORT_ON_LEFT = FlightWaypointTypeConstant(
    "LANDING_102",
    _("landing (short on left)"),
  )
  LANDING_SHORT_ON_RIGHT = FlightWaypointTypeConstant(
    "LANDING_103",
    _("landing (short on right)"),
  )
  LANDING_STRAIGHT = FlightWaypointTypeConstant(
    "LANDING_104",
    _("landing (straight)"),
  )
