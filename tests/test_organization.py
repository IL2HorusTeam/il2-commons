# coding: utf-8
from __future__ import unicode_literals

import unittest

from candv import Constants, SimpleConstant, Values, with_constant_class
from verboselib import use_language, drop_language

from il2fb.commons.organization import (
    Belligerents, Country, Countries, AirForce, AirForces, Regiment, Regiments,
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


class RegimentTestCase(unittest.TestCase):

    def tearDown(self):
        drop_language()

    def test_create_regiment(self):
        r = Regiment(AirForces.vvs_rkka, 'foo')
        self.assertEqual(r.air_force, AirForces.vvs_rkka)
        self.assertEqual(r.code_name, 'foo')

    def test_unknown_verbose_name(self):
        r = Regiment(AirForces.vvs_rkka, 'foo')

        use_language('en')
        self.assertEqual(r.verbose_name, "")

        use_language('ru')
        self.assertEqual(r.verbose_name, "")

        use_language('ja')
        self.assertEqual(r.verbose_name, "")

    def test_valid_verbose_name(self):
        r = Regiment(AirForces.vvs_rkka, '1st_AE_1AR')

        use_language('en')
        self.assertEqual(r.verbose_name, "OIR AE of 1st AG VVS")

        use_language('ru')
        self.assertEqual(r.verbose_name, "ОИРАЭ 1-й АГ")

        use_language('ja')
        self.assertEqual(r.verbose_name, "OIR AE of 1st AG VVS")

    def test_verbose_name_missing_translation(self):
        r = Regiment(AirForces.usn, 'USN_VT_9B')

        use_language('en')
        self.assertEqual(r.verbose_name, "VT-9 USS Essex CV-9")

        use_language('ru')
        self.assertEqual(r.verbose_name, "VT-9 USS Essex CV-9")

        use_language('ja')
        self.assertEqual(r.verbose_name, "VT-9 USS Essex CV-9")

    def test_unknown_help_text(self):
        r = Regiment(AirForces.vvs_rkka, 'foo')

        use_language('en')
        self.assertEqual(r.help_text, "")

        use_language('ru')
        self.assertEqual(r.help_text, "")

        use_language('ja')
        self.assertEqual(r.help_text, "")

    def test_valid_help_text(self):
        r = Regiment(AirForces.vvs_rkka, '1st_AE_1AR')

        use_language('en')
        self.assertEqual(r.help_text, "OIR AE of 1st AG VVS")

        use_language('ru')
        self.assertEqual(
            r.help_text,
            "Отдельная Истребительно-Разведываетльния Авиаэскадрилья "
            "1-й Авиагруппы"
        )  # yes, there are mistakes in word 'Разведываетльния'

        use_language('ja')
        self.assertEqual(r.help_text, "OIR AE of 1st AG VVS")

    def test_help_text_missing_translation(self):
        r = Regiment(AirForces.usn, 'USN_VT_9B')

        self.assertEqual(r.help_text, "US Navy Torpedo Squadron 9 USS Essex CV-9")

        use_language('en')
        self.assertEqual(r.help_text, "US Navy Torpedo Squadron 9 USS Essex CV-9")

        use_language('ru')
        self.assertEqual(r.help_text, "US Navy Torpedo Squadron 9 USS Essex CV-9")

        use_language('ja')
        self.assertEqual(r.help_text, "US Navy Torpedo Squadron 9 USS Essex CV-9")

    def test_unknown_attributes(self):
        r = Regiment(AirForces.usn, 'USN_VT_9B')
        self.assertRaises(AttributeError, getattr, r, 'abracadabra')

    def test_repr(self):
        r = Regiment(AirForces.usn, 'USN_VT_9B')
        self.assertEqual(repr(r), "<Regiment 'USN_VT_9B'>")

    def test_to_primitive(self):
        primitive = Regiment(AirForces.usn, 'USN_VT_9B').to_primitive()

        self.assertEqual(primitive.pop('code_name'), "USN_VT_9B")
        self.assertEqual(primitive.pop('verbose_name'), "VT-9 USS Essex CV-9")
        self.assertEqual(primitive.pop('help_text'), "US Navy Torpedo Squadron 9 USS Essex CV-9")

        air_force = primitive.pop('air_force')
        self.assertEqual(air_force.pop('name'), "usn")
        self.assertEqual(air_force.pop('default_flight_prefix'), "UN_NN")
        self.assertEqual(air_force.pop('value'), "un")
        self.assertEqual(air_force.pop('verbose_name'), "USN")
        self.assertEqual(air_force.pop('help_text'), "United States Navy")

        country = air_force.pop('country')
        self.assertEqual(country.pop('name'), "us")
        self.assertEqual(country.pop('verbose_name'), "United States")
        self.assertIsNone(country.pop('help_text'))

        belligerent = country.pop('belligerent')
        self.assertEqual(belligerent.pop('name'), "red")
        self.assertEqual(belligerent.pop('verbose_name'), "allies")
        self.assertIsNone(belligerent.pop('help_text'))
        self.assertEqual(belligerent.pop('value'), 1)

        self.assertFalse(belligerent)
        self.assertFalse(country)
        self.assertFalse(air_force)
        self.assertFalse(primitive)


class RegimentsTestCase(unittest.TestCase):

    def test_create_regiments(self):

        def create():
            Regiments()

        self.assertRaises(TypeError, create)

    def test_get_by_code_name(self):
        r = Regiments.get_by_code_name('1GvIAP')
        self.assertEqual(r.air_force,  AirForces.vvs_rkka)

        # test cache
        r = Regiments.get_by_code_name('1GvIAP')

    def test_get_by_code_name_invalid(self):
        self.assertRaises(ValueError, Regiments.get_by_code_name, 'foo')

    def test_filter_by_air_force(self):
        regiments = Regiments.filter_by_air_force(AirForces.ala)
        self.assertEquals(len(regiments), 1)

        r = Regiments.get_by_code_name('NN')
        self.assertEquals(regiments[0], r)

        # test cache
        regiments = Regiments.filter_by_air_force(AirForces.ala)
