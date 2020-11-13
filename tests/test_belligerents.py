import unittest

from candv import Constants
from candv import SimpleConstant
from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from il2fb.commons import Belligerent
from il2fb.commons import Belligerents


class BelligerentsTestCase(unittest.TestCase):

  def test_to_group(self):

    class FOO(with_constant_class(Belligerent), Values):
      bar = Belligerent(
        value=999,
        color="000000",
        verbose_name="bar",
      ).to_group(
        group_class=Constants,
        qux=SimpleConstant(),
      )

    self.assertEqual(FOO.bar.color, "000000")
    self.assertEqual(FOO.bar.names(), ["qux", ])

  def test_to_primitive(self):

    class FOO(with_constant_class(Belligerent), Values):
      bar = Belligerent(
        value=999,
        color="000000",
        verbose_name="bar",
      )

    self.assertEqual(
      FOO.bar.to_primitive(),
      {
        'name': "bar",
        'value': 999,
        'color': "000000",
        'verbose_name': "bar",
        'help_text': None,
      }
    )
