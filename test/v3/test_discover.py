import unittest
from fulltmdb import Discover

# alot more tests to add here


class DiscoverTest(unittest.TestCase):
    def test_get_details(self):
        result = Discover.movie(page=1)
        self.assertTrue('results' in result)

    def test_get_tv_change_list(self):
        params = {'page':1}
        result = Discover.tv(params=params)
        self.assertTrue('results' in result)
