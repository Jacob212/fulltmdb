import unittest
from fulltmdb import Collections


class CollectionsTest(unittest.TestCase):
    def test_details(self):
        result = Collections.details(10)
        self.assertTrue('id' in result)

    def test_images(self):
        result = Collections.images(10)
        self.assertTrue('id' in result)

    def test_translations(self):
        result = Collections.translations(10)
        self.assertTrue('id' in result)
