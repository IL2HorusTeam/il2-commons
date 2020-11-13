import unittest

from il2fb.commons import Skills


class CommonsTestCase(unittest.TestCase):

    def test_skills(self):
        self.assertEqual(
            [(x.name, x.value) for x in Skills.constants()],
            [
                ('rookie', 0),
                ('average', 1),
                ('veteran', 2),
                ('ace', 3),
            ]
        )
