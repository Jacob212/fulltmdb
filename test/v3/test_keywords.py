import unittest
from fulltmdb import keywords


class KeywordsTest(unittest.TestCase):
    def test_get_details(self):
        result = keywords.get_details(3417)
        self.assertTrue('name' in result)

    def test_get_movies(self):
        result = keywords.get_movies(3417)
        self.assertTrue('results' in result)
