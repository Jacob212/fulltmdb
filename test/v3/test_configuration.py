import unittest
from fulltmdb import Configuration


class ConfigurationTest(unittest.TestCase):
    def test_api(self):
        result = Configuration.api()
        self.assertTrue('images' in result)

    def test_countries(self):
        result = Configuration.countries()
        self.assertTrue(type(result) == list)

    def test_jobs(self):
        result = Configuration.jobs()
        self.assertTrue(type(result) == list)

    def test_languages(self):
        result = Configuration.languages()
        self.assertTrue(type(result) == list)

    def test_primary_translations(self):
        result = Configuration.primary_translations()
        self.assertTrue(type(result) == list)

    def test_timezones(self):
        result = Configuration.timezones()
        self.assertTrue(type(result) == list)
