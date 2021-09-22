import unittest
from fulltmdb import Keywords


class KeywordsTest(unittest.TestCase):
    def test_details(self):
        result = Keywords.details(3417)
        self.assertTrue('name' in result)

    def test_movies(self):
        result = Keywords.movies(3417)
        self.assertTrue('results' in result)
