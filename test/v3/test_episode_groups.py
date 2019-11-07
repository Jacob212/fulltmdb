import unittest
from fulltmdb import episode_groups


class EpisodeGroupsTest(unittest.TestCase):
    def test_details(self):
        result = episode_groups.details('5acf93e60e0a26346d0000ce')
        self.assertTrue('groups' in result)