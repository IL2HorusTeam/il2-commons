import unittest

from il2fb.commons.supported_languages import SUPPORTED_LANGUAGES


class SupportedLanguagesTestCase(unittest.TestCase):

  def test_names(self):
    self.assertEqual(SUPPORTED_LANGUAGES.names(), ["EN", "RU", ])

  def test_default_language(self):
    self.assertEqual(SUPPORTED_LANGUAGES.get_default().name, "EN")
