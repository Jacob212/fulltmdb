import unittest
from fulltmdb import collections

class CollectionsTest(unittest.TestCase):
    def test_get_details(self):
        result = collections.get_details(10)
        self.assertTrue(hasattr(result, 'id'))

    def test_get_images(self):
        result = collections.get_images(10)
        self.assertTrue(hasattr(result, 'id'))

    def test_get_translations(self):
        result = collections.get_translations(10)
        self.assertTrue(hasattr(result, 'id'))
