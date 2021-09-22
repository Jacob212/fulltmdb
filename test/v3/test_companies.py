import unittest
from fulltmdb import Companies


class CompaniesTest(unittest.TestCase):
    def test_details(self):
        result = Companies.details(1)
        self.assertTrue('id' in result)

    def test_alternative_names(self):
        result = Companies.alternative_names(1)
        self.assertTrue('id' in result)

    def test_images(self):
        result = Companies.images(1)
        self.assertTrue('id' in result)
