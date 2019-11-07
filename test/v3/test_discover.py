import unittest
from fulltmdb import discover

# alot more tests to add here


class DiscoverTest(unittest.TestCase):
    def test_get_details(self):
        result = discover.movie(year=2019)
        self.assertTrue('results' in result)
        self.assertTrue(result['results'][0]['id'] == 475557)

    def test_get_tv_change_list(self):
        result = discover.tv(page=2)
        self.assertTrue('results' in result)
