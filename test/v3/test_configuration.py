import unittest
from fulltmdb import configuration


class ConfigurationTest(unittest.TestCase):
    def test_api(self):
        result = configuration.api()
        self.assertTrue('images' in result)

    def test_countries(self):
        result = configuration.countries()
        self.assertTrue(type(result) == list)

    def test_jobs(self):
        result = configuration.jobs()
        self.assertTrue(type(result) == list)

    def test_languages(self):
        result = configuration.languages()
        self.assertTrue(type(result) == list)

    def test_primary_translations(self):
        result = configuration.primary_translations()
        self.assertTrue(type(result) == list)

    def test_timezones(self):
        result = configuration.timezones()
        self.assertTrue(type(result) == list)
