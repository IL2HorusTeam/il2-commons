import unittest

from candv import Constants
from candv import SimpleConstant
from candv import Values
from candv import with_constant_class

from il2fb.commons.organization import Countries
from il2fb.commons.organization import AirForce
from il2fb.commons.organization import AirForces


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
