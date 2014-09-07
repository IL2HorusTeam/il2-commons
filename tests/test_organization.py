# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from candv import Constants, SimpleConstant, Values

from il2fb.commons.organization import (
    Belligerents, Country, Countries, AirForce, AirForces, Regiment, Regiments,
)


class BelligerentsTestCase(unittest.TestCase):

    def test_belligerents(self):
        data = [(x.name, x.value) for x in Belligerents.constants()]
        self.assertEqual(data, [
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
        ])


class CountriesTestCase(unittest.TestCase):

    def test_country_as_group(self):

        class FOO(Values):
            constant_class = Country

            bar = Country(Belligerents.red, "Bar").to_group(
                Constants,
                qux=SimpleConstant())

        self.assertEqual(FOO.bar.belligerent, Belligerents.red)
        self.assertEqual(FOO.bar.names(), ['qux', ])

    def test_filter_by_belligerent(self):
        self.assertEqual(
            list(Countries.filter_by_belligerent(Belligerents.none)), [])
        self.assertEqual(
            list(Countries.filter_by_belligerent(Belligerents.red)),
            [Countries.au, Countries.fr, Countries.nl, Countries.nz,
             Countries.pl, Countries.su, Countries.uk, Countries.us, ])


class AirForcesTestCase(unittest.TestCase):

    def test_air_force_as_group(self):

        class FOO(Values):
            constant_class = AirForce

            bar = (
                AirForce(
                    country=Countries.au,
                    default_flight_prefix='brrr',
                    value='br',
                    verbose_name="BAR")
                .to_group(
                    Constants,
                    qux=SimpleConstant())
            )

        self.assertEqual(FOO.bar.country, Countries.au)
        self.assertEqual(FOO.bar.default_flight_prefix, 'brrr')
        self.assertEqual(FOO.bar.names(), ['qux', ])

    def test_get_flight_prefixes(self):
        self.assertEqual(
            list(AirForces.get_flight_prefixes()),
            [
                'fr01', 'f01', 'ro01', 'h01', 'g01', 'ja01', 'IN_NN', 'pl01',
                'i01', 'RA_NN', 'gb01', 'RN_NN', 'DU_NN', 'RZ_NN', 'sk01',
                'usa01', 'UM_NN', 'UN_NN', 'r01',
            ])

    def test_get_by_flight_prefix(self):
        self.assertEqual(AirForces.get_by_flight_prefix('r01'),
                         AirForces.vvs_rkka)
        self.assertRaises(ValueError, AirForces.get_by_flight_prefix, 'foo')

    def test_filter_by_country(self):
        self.assertEqual(list(AirForces.filter_by_country(Countries.su)),
                         [AirForces.vvs_rkka, ])
        self.assertEqual(list(AirForces.filter_by_country(Countries.us)),
                         [AirForces.usaaf, AirForces.usmc, AirForces.usn, ])

    def test_filter_by_belligerent(self):
        self.assertEqual(
            list(AirForces.filter_by_belligerent(Belligerents.none)), [])
        self.assertEqual(
            list(AirForces.filter_by_belligerent(Belligerents.red)),
            [
                AirForces.ala, AirForces.paf, AirForces.raaf, AirForces.raf,
                AirForces.rn, AirForces.rnlaf, AirForces.rnzaf, AirForces.usaaf,
                AirForces.usmc, AirForces.usn, AirForces.vvs_rkka,
            ])


class RegimentTestCase(unittest.TestCase):

    def test_create_regiment(self):
        r = Regiment(AirForces.vvs_rkka, 'foo')
        self.assertEqual(r.air_force, AirForces.vvs_rkka)
        self.assertEqual(r.code_name, 'foo')

    def test_unknown_verbose_name(self):
        r = Regiment(AirForces.vvs_rkka, 'foo')

        self.assertEqual(r.verbose_name_en, "")
        self.assertEqual(r.verbose_name_ru, "")
        self.assertEqual(r.verbose_name_some, "")

    def test_valid_verbose_name(self):
        r = Regiment(AirForces.vvs_rkka, '1st_AE_1AR')

        self.assertEqual(r.verbose_name_en, "OIR AE of 1st AG VVS")
        self.assertEqual(r.verbose_name_ru, "ОИРАЭ 1-й АГ")
        self.assertEqual(r.verbose_name_some, "OIR AE of 1st AG VVS")

    def test_verbose_name_missing_translation(self):
        r = Regiment(AirForces.usn, 'USN_VT_9B')

        self.assertEqual(r.verbose_name_en, "VT-9, USS Essex CV-9")
        self.assertEqual(r.verbose_name_ru, "VT-9, USS Essex CV-9")
        self.assertEqual(r.verbose_name_some, "VT-9, USS Essex CV-9")

    def test_unknown_help_text(self):
        r = Regiment(AirForces.vvs_rkka, 'foo')

        self.assertEqual(r.help_text_en, "")
        self.assertEqual(r.help_text_ru, "")
        self.assertEqual(r.help_text_some, "")

    def test_valid_help_text(self):
        r = Regiment(AirForces.vvs_rkka, '1st_AE_1AR')

        self.assertEqual(r.help_text_en, "OIR AE of 1st AG VVS")
        self.assertEqual(
            r.help_text_ru,
            "Отдельная Истребительно-Разведываетльния Авиаэскадрилья "
            "1-й Авиагруппы"
        )  # yes, there are mistakes in word 'Разведываетльния'
        self.assertEqual(r.help_text_some, "OIR AE of 1st AG VVS")

    def test_help_text_missing_translation(self):
        r = Regiment(AirForces.usn, 'USN_VT_9B')

        self.assertEqual(r.help_text_en, "US Navy VT-9, USS Essex CV-9")
        self.assertEqual(r.help_text_ru, "US Navy VT-9, USS Essex CV-9")
        self.assertEqual(r.help_text_some, "US Navy VT-9, USS Essex CV-9")

    def test_unknown_attributes(self):
        r = Regiment(AirForces.usn, 'USN_VT_9B')

        def _getattr(name):
            return getattr(r, name)

        self.assertRaises(AttributeError, _getattr, 'abracadabra')

        self.assertRaises(AttributeError, _getattr, 'verbose_name')
        self.assertRaises(AttributeError, _getattr, 'verbose_name_')

        self.assertRaises(AttributeError, _getattr, 'help_text')
        self.assertRaises(AttributeError, _getattr, 'help_text_')


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
