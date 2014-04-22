# -*- coding: utf-8 -*-
import unittest

from il2_commons import SupportedLanguages, GameVersions, Skills


class IL2CommonsTestCase(unittest.TestCase):

    def test_languages(self):
        self.assertEqual(SupportedLanguages.names(), ['en', 'ru', ])
        self.assertEqual(SupportedLanguages.get_default(),
                         SupportedLanguages.en)

    def test_game_versions(self):
        self.assertEqual(GameVersions.values(), ['4.12', '4.12.1', '4.12.2', ])

    def test_skills(self):
        data = [(x.name, x.value) for x in Skills.constants()]
        self.assertEqual(data, [('rookie', 0),
                                ('average', 1),
                                ('veteran', 2),
                                ('ace', 3), ])
