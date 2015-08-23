# -*- coding: utf-8 -*-

import unittest

from il2fb.commons import SupportedLanguages, Skills


class CommonsTestCase(unittest.TestCase):

    def test_languages(self):
        self.assertEqual(SupportedLanguages.names(), ['en', 'ru', ])
        self.assertEqual(
            SupportedLanguages.get_default(),
            SupportedLanguages.en
        )

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
