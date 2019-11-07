import unittest
from fulltmdb import networks


class NetworksTest(unittest.TestCase):
    def test_details(self):
        result = networks.details(213)
        self.assertTrue('name' in result)

    def test_alternative_names(self):
        result = networks.alternative_names(174)
        self.assertTrue('results' in result)

    def test_images(self):
        result = networks.images(213)
        self.assertTrue('logos' in result)
