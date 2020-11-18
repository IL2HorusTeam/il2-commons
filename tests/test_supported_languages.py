import unittest

from il2fb.commons.supported_languages import SUPPORTED_LANGUAGE


class SupportedLanguagesTestCase(unittest.TestCase):

  def test_names(self):
    self.assertEqual(SUPPORTED_LANGUAGE.names(), ["EN", "RU", ])

  def test_default_language(self):
    self.assertEqual(SUPPORTED_LANGUAGE.get_default().name, "EN")
