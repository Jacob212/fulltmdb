import unittest
from fulltmdb import keywords


class KeywordsTest(unittest.TestCase):
    def test_details(self):
        result = keywords.details(3417)
        self.assertTrue('name' in result)

    def test_movies(self):
        result = keywords.movies(3417)
        self.assertTrue('results' in result)
