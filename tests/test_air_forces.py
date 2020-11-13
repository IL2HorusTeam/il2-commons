import unittest

from candv import Constants
from candv import SimpleConstant
from candv import Values
from candv import with_constant_class

from il2fb.commons import AirForceConstant
from il2fb.commons import AIR_FORCE
from il2fb.commons import COUNTRY
from il2fb.commons import IL2FBLookupError


class AirForcesTestCase(unittest.TestCase):

  def test_to_group(self):

    class FOO(with_constant_class(AirForceConstant), Values):
      BAR = AirForceConstant(
        country=COUNTRY.AU,
        default_flight_prefix="brrr",
        value="br",
        verbose_name="BAR",
      ).to_group(
        group_class=Constants,
        qux=SimpleConstant(),
      )

    self.assertEqual(FOO.BAR.country, COUNTRY.AU)
    self.assertEqual(FOO.BAR.default_flight_prefix, "brrr")
    self.assertEqual(FOO.BAR.names(), ["qux", ])

  def test_to_primitive(self):

    class FOO(with_constant_class(AirForceConstant), Values):
      BAR = AirForceConstant(
        country=COUNTRY.AU,
        default_flight_prefix="brrr",
        value="br",
        verbose_name="BAR",
      )

    self.assertEqual(
      FOO.BAR.to_primitive(),
      {
        'name': "BAR",
        'country': {
          'name': "AU",
          'verbose_name': "Australia",
          'help_text': None,
        },
        'default_flight_prefix': "brrr",
        'value': "br",
        'verbose_name': "BAR",
        'help_text': None,
      }
    )

  def test_get_flight_prefixes(self):
    self.assertEqual(
      list(AIR_FORCE.get_flight_prefixes()),
      [
        "fr01", "f01", "ro01", "h01", "g01", "ja01", "IN_NN", "pl01", "i01",
        "RA_NN", "gb01", "RN_NN", "DU_NN", "RZ_NN", "sk01", "usa01", "UM_NN",
        "UN_NN", "r01", None,
      ]
    )

  def test_get_by_flight_prefix(self):
    self.assertEqual(
      AIR_FORCE.get_by_flight_prefix("r01"),
      AIR_FORCE.VVS_RKKA
    )
    self.assertRaises(IL2FBLookupError, AIR_FORCE.get_by_flight_prefix, "foo")

  def test_filter_by_country(self):
    self.assertEqual(
      list(AIR_FORCE.filter_by_country(COUNTRY.SU)),
      [AIR_FORCE.VVS_RKKA, ]
    )
    self.assertEqual(
      list(AIR_FORCE.filter_by_country(COUNTRY.US)),
      [AIR_FORCE.USAAF, AIR_FORCE.USMC, AIR_FORCE.USN, ]
    )
