import unittest
from fulltmdb import credits

class CreditsTest(unittest.TestCase):
    def test_get_details(self):
        result = credits.get_details("52542282760ee313280017f9")
        self.assertTrue(hasattr(result, 'id'))
