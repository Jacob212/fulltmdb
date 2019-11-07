import unittest
from fulltmdb import trending


class TrendingTest(unittest.TestCase):
    def test_trending(self):
        result = trending.trending('all', 'day')
        self.assertTrue('results' in result)
