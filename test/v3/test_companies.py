import unittest
from fulltmdb import companies


class CompaniesTest(unittest.TestCase):
    def test_details(self):
        result = companies.details(1)
        self.assertTrue('id' in result)

    def test_alternative_names(self):
        result = companies.alternative_names(1)
        self.assertTrue('id' in result)

    def test_images(self):
        result = companies.images(1)
        self.assertTrue('id' in result)
