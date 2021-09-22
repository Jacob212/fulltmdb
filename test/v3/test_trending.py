import unittest
from fulltmdb import Trending


class TrendingTest(unittest.TestCase):
    def test_trending(self):
        result = Trending.trending('all', 'day')
        self.assertTrue('results' in result)
