import unittest

from candv import Constants
from candv import SimpleConstant
from candv import Values
from candv import with_constant_class

from il2fb.commons.air_forces import AirForceConstant
from il2fb.commons.air_forces import AIR_FORCES

from il2fb.commons.countries  import COUNTRIES
from il2fb.commons.exceptions import IL2FBLookupError


class AirForcesTestCase(unittest.TestCase):

  def test_to_group(self):

    class FOO(with_constant_class(AirForceConstant), Values):
      BAR = AirForceConstant(
        country=COUNTRIES.AU,
        default_regiment_id="brrr",
        value="br",
        verbose_name="BAR",
      ).to_group(
        group_class=Constants,
        qux=SimpleConstant(),
      )

    self.assertEqual(FOO.BAR.country, COUNTRIES.AU)
    self.assertEqual(FOO.BAR.default_regiment_id, "brrr")
    self.assertEqual(FOO.BAR.names(), ["qux", ])

  def test_to_primitive(self):

    class FOO(with_constant_class(AirForceConstant), Values):
      BAR = AirForceConstant(
        country=COUNTRIES.AU,
        default_regiment_id="brrr",
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
        'default_regiment_id': "brrr",
        'value': "br",
        'verbose_name': "BAR",
        'help_text': None,
      }
    )

  def test_get_default_regiment_ids(self):
    self.assertEqual(
      list(AIR_FORCES.get_default_regiment_ids()),
      [
        "fr01", "f01", "ro01", "h01", "g01", "ja01", "IN_NN", "pl01", "i01",
        "RA_NN", "gb01", "RN_NN", "DU_NN", "RZ_NN", "sk01", "usa01", "UM_NN",
        "UN_NN", "r01", None,
      ]
    )

  def test_get_by_default_regiment_id(self):
    self.assertEqual(
      AIR_FORCES.get_by_default_regiment_id("r01"),
      AIR_FORCES.VVS_RKKA
    )

  def test_get_by_default_regiment_id_invalid_value(self):
    self.assertRaises(IL2FBLookupError, AIR_FORCES.get_by_default_regiment_id, "foo")

  def test_filter_by_country(self):
    self.assertEqual(
      list(AIR_FORCES.filter_by_country(COUNTRIES.SU)),
      [AIR_FORCES.VVS_RKKA, ]
    )
    self.assertEqual(
      list(AIR_FORCES.filter_by_country(COUNTRIES.US)),
      [AIR_FORCES.USAAF, AIR_FORCES.USMC, AIR_FORCES.USN, ]
    )
