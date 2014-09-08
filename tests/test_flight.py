# -*- coding: utf-8 -*-
import unittest

from il2fb.commons.flight import Formations, RoutePointTypes


class FlightTestCase(unittest.TestCase):

    def test_formations(self):
        data = [(x.name, x.value) for x in Formations.constants()]
        self.assertEqual(data, [
            ('echelon_right', 'F2'),
            ('echelon_left', 'F3'),
            ('line_abreast', 'F4'),
            ('line_asteam', 'F5'),
            ('vic', 'F6'),
            ('finger_four', 'F7'),
            ('diamond', 'F8'),
        ])

    def test_waypoint_types(self):
        data = [(x.name, x.value) for x in RoutePointTypes.constants()]
        self.assertEqual(data, [
            ('takeoff_normal', 'TAKEOFF'),
            ('takeoff_pair', 'TAKEOFF_002'),
            ('takeoff_in_line', 'TAKEOFF_003'),

            ('taxiing', 'TAKEOFF_004'),
            ('normal', 'NORMFLY'),
            ('air_attack', 'X_AIR_ATTACK'),
            ('ground_attack', 'GATTACK'),

            ('patrol_triangle', 'NORMFLY_401'),
            ('patrol_square', 'NORMFLY_402'),
            ('patrol_pentagon', 'NORMFLY_403'),
            ('patrol_hexagon', 'NORMFLY_404'),
            ('patrol_random', 'NORMFLY_405'),

            ('artillery_spotter', 'NORMFLY_407'),

            ('landing_on_left', 'LANDING'),
            ('landing_on_right', 'LANDING_101'),
            ('landing_short_on_left', 'LANDING_102'),
            ('landing_short_on_right', 'LANDING_103'),
            ('landing_straight', 'LANDING_104'),
        ])
