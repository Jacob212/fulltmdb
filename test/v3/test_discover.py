import unittest
from fulltmdb import discover

# alot more tests to add here


class DiscoverTest(unittest.TestCase):
    def test_get_details(self):
        result = discover.movie(page=1)
        self.assertTrue('results' in result)

    def test_get_tv_change_list(self):
        params = {'page':1}
        result = discover.tv(params=params)
        self.assertTrue('results' in result)
