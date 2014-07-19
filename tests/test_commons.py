# -*- coding: utf-8 -*-
import unittest

from il2fb.commons import SUPPORTED_LANGUAGES, GAME_VERSIONS, SKILLS


class CommonsTestCase(unittest.TestCase):

    def test_languages(self):
        self.assertEqual(SUPPORTED_LANGUAGES.names(), ['en', 'ru', ])
        self.assertEqual(SUPPORTED_LANGUAGES.get_default(),
                         SUPPORTED_LANGUAGES.en)

    def test_game_versions(self):
        self.assertEqual(GAME_VERSIONS.values(), [
            '4.12', '4.12.1', '4.12.2',
        ])

    def test_skills(self):
        data = [(x.name, x.value) for x in SKILLS.constants()]
        self.assertEqual(data, [
            ('rookie', 0),
            ('average', 1),
            ('veteran', 2),
            ('ace', 3),
        ])
