import unittest

from il2fb.commons import SKILL


class SkillsTestCase(unittest.TestCase):

  def test_skills(self):
    self.assertEqual(
      [(x.name, x.value) for x in SKILL.constants()],
      [
        ("ROOKIE",  0),
        ("AVERAGE", 1),
        ("VETERAN", 2),
        ("ACE",     3),
      ]
    )
