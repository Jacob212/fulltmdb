import unittest
from fulltmdb import collections


class CollectionsTest(unittest.TestCase):
    def test_details(self):
        result = collections.details(10)
        self.assertTrue('id' in result)

    def test_images(self):
        result = collections.images(10)
        self.assertTrue('id' in result)

    def test_translations(self):
        result = collections.translations(10)
        self.assertTrue('id' in result)
