# -*- coding: utf-8 -*-
from candv import Values, VerboseValueConstant

from il2_commons.utils.translation import ugettext_lazy as _


class Formations(Values):
    echelon_right = VerboseValueConstant('F1', _("echelon right"))
    echelon_left = VerboseValueConstant('F2', _("echelon left"))
    rank = VerboseValueConstant('F3', _("rank"))
    line_abreast = VerboseValueConstant('F4', _("line abreast"))
    line_asteam = VerboseValueConstant('F5', _("line asteam"))
    vic = VerboseValueConstant('F6', _("vic"))
    finger_four = VerboseValueConstant('F7', _("finger four"))
    diamond = VerboseValueConstant('F8', _("diamond"))


class WaypointTypes(Values):
    # Take-off -----------------------------------------------------------------
    takeoff_normal = VerboseValueConstant(
        'TAKEOFF',
        _("takeoff (normal)"))
    takeoff_pair = VerboseValueConstant(
        'TAKEOFF_002',
        _("takeoff (pair)"))
    takeoff_in_line = VerboseValueConstant(
        'TAKEOFF_003',
        _("takeoff (in line)"))

    # Taxiing ------------------------------------------------------------------
    taxiing = VerboseValueConstant(
        'TAKEOFF_004',
        _("taxiing"))

    # Normal flight ------------------------------------------------------------
    normal_fly = VerboseValueConstant(
        'NORMFLY',
        _("normal fly"))

    # Patrol -------------------------------------------------------------------
    patrol_triangle = VerboseValueConstant(
        'NORMFLY_401',
        _("patrol (triangle)"))
    patrol_square = VerboseValueConstant(
        'NORMFLY_402',
        _("patrol (square)"))
    patrol_pentagon = VerboseValueConstant(
        'NORMFLY_403',
        _("patrol (pentagon)"))
    patrol_hexagon = VerboseValueConstant(
        'NORMFLY_404',
        _("patrol (hexagon)"))
    patrol_random = VerboseValueConstant(
        'NORMFLY_405',
        _("patrol (random)"))

    # Langing ------------------------------------------------------------------
    landing_on_left = VerboseValueConstant(
        'LANDING',
        _("landing (on left)"))
    landing_on_right = VerboseValueConstant(
        'LANDING_101',
        _("landing (on right)"))
    landing_short_on_left = VerboseValueConstant(
        'LANDING_102',
        _("landing (short on left)"))
    landing_short_on_right = VerboseValueConstant(
        'LANDING_103',
        _("landing (short on right)"))
    landing_straight = VerboseValueConstant(
        'LANDING_104',
        _("landing (straight)"))
