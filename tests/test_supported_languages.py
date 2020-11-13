import unittest

from il2fb.commons import SupportedLanguages


class SupportedLanguagesTestCase(unittest.TestCase):

  def test_names(self):
    self.assertEqual(SupportedLanguages.names(), ["en", "ru", ])

  def test_default_language(self):
    self.assertEqual(SupportedLanguages.get_default().name, "en")
