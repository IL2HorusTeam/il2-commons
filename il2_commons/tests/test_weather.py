# -*- coding: utf-8 -*-
import unittest

from il2_commons.weather import Conditions, Gust, Turbulence


class WeatherTestCase(unittest.TestCase):

    def test_conditions(self):
        data = [(x.name, x.value) for x in Conditions.constants()]
        self.assertEqual(data, [('clear', 0),
                                ('good', 1),
                                ('hazy', 2),
                                ('poor', 3),
                                ('blind', 4),
                                ('precipitation', 5),
                                ('thunderstorm', 6), ])

    def test_gust(self):
        data = [(x.name, x.value) for x in Gust.constants()]
        self.assertEqual(data, [('none', 0),
                                ('low', 1),
                                ('moderate', 2),
                                ('strong', 3), ])

    def test_turbulence(self):
        data = [(x.name, x.value) for x in Turbulence.constants()]
        self.assertEqual(data, [('none', 0),
                                ('low', 1),
                                ('moderate', 2),
                                ('strong', 3),
                                ('very_strong', 4), ])
