import unittest
from fulltmdb import Networks


class NetworksTest(unittest.TestCase):
    def test_details(self):
        result = Networks.details(213)
        self.assertTrue('name' in result)

    def test_alternative_names(self):
        result = Networks.alternative_names(174)
        self.assertTrue('results' in result)

    def test_images(self):
        result = Networks.images(213)
        self.assertTrue('logos' in result)
