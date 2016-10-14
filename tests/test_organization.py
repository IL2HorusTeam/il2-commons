# coding: utf-8
from __future__ import unicode_literals

import unittest

from candv import Constants, SimpleConstant, Values, with_constant_class

from il2fb.commons.organization import (
    Belligerents, Country, Countries, AirForce, AirForces,
)


class BelligerentsTestCase(unittest.TestCase):

    def test_belligerents(self):
        self.assertEqual(
            [(x.name, x.value) for x in Belligerents.constants()],
            [
                ('none', 0),
                ('red', 1),
                ('blue', 2),
                ('green', 3),
                ('gold', 4),
                ('purple', 5),
                ('aqua', 6),
                ('maroon', 7),
                ('navy', 8),
                ('emerald', 9),
                ('olive', 10),
                ('magenta', 11),
                ('teal', 12),
                ('orange', 13),
                ('turquoise', 14),
                ('brown', 15),
                ('salad', 16),
            ]
        )


class CountriesTestCase(unittest.TestCase):

    def test_to_group(self):

        class FOO(with_constant_class(Country), Values):
            bar = Country(
                belligerent=Belligerents.red,
                verbose_name="Bar",
            ).to_group(
                group_class=Constants,
                qux=SimpleConstant(),
            )

        self.assertEqual(FOO.bar.belligerent, Belligerents.red)
        self.assertEqual(FOO.bar.names(), ['qux', ])

    def test_to_primitive(self):

        class FOO(with_constant_class(Country), Values):
            bar = Country(Belligerents.red, "Bar")

        self.assertEqual(
            FOO.bar.to_primitive(),
            {
                'name': 'bar',
                'verbose_name': "Bar",
                'help_text': None,
                'belligerent': {
                    'name': 'red',
                    'verbose_name': "allies",
                    'help_text': None,
                    'value': 1,
                }
            }
        )

    def test_filter_by_belligerent(self):
        self.assertEqual(
            list(Countries.filter_by_belligerent(Belligerents.none)),
            []
        )
        self.assertEqual(
            list(Countries.filter_by_belligerent(Belligerents.red)),
            [
                Countries.au, Countries.fr, Countries.nl, Countries.nz,
                Countries.pl, Countries.su, Countries.uk, Countries.us,
            ]
        )


class AirForcesTestCase(unittest.TestCase):

    def test_to_group(self):

        class FOO(with_constant_class(AirForce), Values):
            bar = AirForce(
                country=Countries.au,
                default_flight_prefix='brrr',
                value='br',
                verbose_name="BAR",
            ).to_group(
                group_class=Constants,
                qux=SimpleConstant(),
            )

        self.assertEqual(FOO.bar.country, Countries.au)
        self.assertEqual(FOO.bar.default_flight_prefix, 'brrr')
        self.assertEqual(FOO.bar.names(), ['qux', ])

    def test_to_primitive(self):

        class FOO(with_constant_class(AirForce), Values):
            bar = AirForce(
                country=Countries.au,
                default_flight_prefix='brrr',
                value='br',
                verbose_name="BAR",
            )

        self.assertEqual(
            FOO.bar.to_primitive(),
            {
                'name': "bar",
                'country': {
                    'name': 'au',
                    'verbose_name': "Australia",
                    'help_text': None,
                    'belligerent': {
                        'name': 'red',
                        'verbose_name': "allies",
                        'help_text': None,
                        'value': 1,
                    }
                },
                'default_flight_prefix': 'brrr',
                'value': 'br',
                'verbose_name': "BAR",
                'help_text': None,
            }
        )

    def test_get_flight_prefixes(self):
        self.assertEqual(
            list(AirForces.get_flight_prefixes()),
            [
                'fr01', 'f01', 'ro01', 'h01', 'g01', 'ja01', 'IN_NN', 'pl01',
                'i01', 'RA_NN', 'gb01', 'RN_NN', 'DU_NN', 'RZ_NN', 'sk01',
                'usa01', 'UM_NN', 'UN_NN', 'r01', None,
            ]
        )

    def test_get_by_flight_prefix(self):
        self.assertEqual(
            AirForces.get_by_flight_prefix('r01'),
            AirForces.vvs_rkka
        )
        self.assertRaises(ValueError, AirForces.get_by_flight_prefix, 'foo')

    def test_filter_by_country(self):
        self.assertEqual(
            list(AirForces.filter_by_country(Countries.su)),
            [AirForces.vvs_rkka, ]
        )
        self.assertEqual(
            list(AirForces.filter_by_country(Countries.us)),
            [AirForces.usaaf, AirForces.usmc, AirForces.usn, ]
        )

    def test_filter_by_belligerent(self):
        self.assertEqual(
            list(AirForces.filter_by_belligerent(Belligerents.none)),
            []
        )
        self.assertEqual(
            list(AirForces.filter_by_belligerent(Belligerents.red)),
            [
                AirForces.ala, AirForces.paf, AirForces.raaf, AirForces.raf,
                AirForces.rn, AirForces.rnlaf, AirForces.rnzaf,
                AirForces.usaaf, AirForces.usmc, AirForces.usn,
                AirForces.vvs_rkka,
            ]
        )
