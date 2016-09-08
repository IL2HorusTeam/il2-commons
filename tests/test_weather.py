# -*- coding: utf-8 -*-

import unittest

from il2fb.commons.weather import Conditions, Gust, Turbulence


class WeatherTestCase(unittest.TestCase):

    def test_conditions(self):
        self.assertEqual(
            [(x.name, x.value) for x in Conditions.constants()],
            [
                ('clear', 0),
                ('good', 1),
                ('hazy', 2),
                ('poor', 3),
                ('blind', 4),
                ('precipitation', 5),
                ('thunderstorm', 6),
            ]
        )

    def test_gust(self):
        self.assertEqual(
            [(x.name, x.value) for x in Gust.constants()],
            [
                ('none', 0),
                ('low', 8),
                ('moderate', 10),
                ('strong', 12),
            ],
        )

    def test_turbulence(self):
        self.assertEqual(
            [(x.name, x.value) for x in Turbulence.constants()],
            [
                ('none', 0),
                ('low', 3),
                ('moderate', 4),
                ('strong', 5),
                ('very_strong', 6),
            ]
        )
