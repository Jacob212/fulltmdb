import unittest
from fulltmdb import networks

class NetworksTest(unittest.TestCase):
    def test_get_details(self):
        result = networks.get_details(213)
        self.assertTrue('name' in result)

    def test_get_alternative_names(self):
        result = networks.get_alternative_names(174)
        self.assertTrue('results' in result)

    def test_get_images(self):
        result = networks.get_images(213)
        self.assertTrue('logos' in result)
