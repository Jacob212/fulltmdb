import unittest
from fulltmdb import trending


class TrendingTest(unittest.TestCase):
    def test_get_trending(self):
        result = trending.get_trending('all', 'day')
        self.assertTrue('results' in result)
