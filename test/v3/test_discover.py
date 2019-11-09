import unittest
from fulltmdb import discover

# alot more tests to add here


class DiscoverTest(unittest.TestCase):
    def test_get_details(self):
        result = discover.movie()
        self.assertTrue('results' in result)

    def test_get_tv_change_list(self):
        result = discover.tv()
        self.assertTrue('results' in result)
