import unittest
from fulltmdb import credits


class CreditsTest(unittest.TestCase):
    def test_details(self):
        result = credits.details("52542282760ee313280017f9")
        self.assertTrue('id' in result)
