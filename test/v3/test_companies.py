import unittest
from fulltmdb import companies


class CompaniesTest(unittest.TestCase):
    def test_get_details(self):
        result = companies.get_details(1)
        self.assertTrue('id' in result)

    def test_get_alternative_names(self):
        result = companies.get_alternative_names(1)
        self.assertTrue('id' in result)

    def test_get_images(self):
        result = companies.get_images(1)
        self.assertTrue('id' in result)
