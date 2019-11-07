import unittest
from fulltmdb import configuration


class ConfigurationTest(unittest.TestCase):
    def test_get_api_configuration(self):
        result = configuration.get_api_configuration()
        self.assertTrue('images' in result)

    def test_get_countries(self):
        result = configuration.get_countries()
        self.assertTrue(type(result) == list)

    def test_get_jobs(self):
        result = configuration.get_jobs()
        self.assertTrue(type(result) == list)

    def test_get_languages(self):
        result = configuration.get_languages()
        self.assertTrue(type(result) == list)

    def test_get_primary_translations(self):
        result = configuration.get_primary_translations()
        self.assertTrue(type(result) == list)

    def test_get_timezones(self):
        result = configuration.get_timezones()
        self.assertTrue(type(result) == list)
