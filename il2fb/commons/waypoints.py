from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from ._translations import gettext_lazy as _
from ._utils import export


@export
class FlightWaypointType(VerboseValueConstant):
  ...


@export
class FlightWaypointTypes(with_constant_class(FlightWaypointType), Values):

  # Take-off ----------------------------------------------------------------
  takeoff_normal = FlightWaypointType(
    'TAKEOFF',
    _("takeoff (normal)"),
  )
  takeoff_pair = FlightWaypointType(
    'TAKEOFF_002',
    _("takeoff (pair)"),
    )
  takeoff_in_line = FlightWaypointType(
    'TAKEOFF_003',
    _("takeoff (in line)"),
  )
  takeoff_taxiing = FlightWaypointType(
    'TAKEOFF_004',
    _("takeoff (taxiing)"),
  )
  takeoff_taxiing_from_static = FlightWaypointType(
    'TAKEOFF_005',
    _("takeoff (taxiing from static)"),
  )

  # Normal flight -----------------------------------------------------------
  normal = FlightWaypointType(
    'NORMFLY',
    _("normal"),
  )

  # Attack ------------------------------------------------------------------
  #: .. warning::
  #:   air attack is not present in game. It is calculated as ``NORMFLY``
  #:   with a target
  air_attack = FlightWaypointType(
    'X_AIR_ATTACK',
    _("air attack"),
  )
  ground_attack = FlightWaypointType(
    'GATTACK',
    _("ground attack"),
  )

  # Patrol ------------------------------------------------------------------
  patrol_triangle = FlightWaypointType(
    'NORMFLY_401',
    _("patrol (triangle)"),
  )
  patrol_square = FlightWaypointType(
    'NORMFLY_402',
    _("patrol (square)"),
  )
  patrol_pentagon = FlightWaypointType(
    'NORMFLY_403',
    _("patrol (pentagon)"),
  )
  patrol_hexagon = FlightWaypointType(
    'NORMFLY_404',
    _("patrol (hexagon)"),
  )
  patrol_random = FlightWaypointType(
    'NORMFLY_405',
    _("patrol (random)"),
  )

  # Artillery spotter -------------------------------------------------------
  artillery_spotter = FlightWaypointType(
    'NORMFLY_407',
    _("artillery spotter"),
  )

  # Langing -----------------------------------------------------------------
  landing_on_left = FlightWaypointType(
    'LANDING',
    _("landing (on left)"),
  )
  landing_on_right = FlightWaypointType(
    'LANDING_101',
    _("landing (on right)"),
  )
  landing_short_on_left = FlightWaypointType(
    'LANDING_102',
    _("landing (short on left)"),
  )
  landing_short_on_right = FlightWaypointType(
    'LANDING_103',
    _("landing (short on right)"),
  )
  landing_straight = FlightWaypointType(
    'LANDING_104',
    _("landing (straight)"),
  )
