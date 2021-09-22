import unittest
from fulltmdb import Find


class FindTest(unittest.TestCase):
    def test_id(self):
        result = Find.id('tt7286456', external_source="imdb_id")
        self.assertTrue('movie_results' in result)
        self.assertTrue(result['movie_results'][0]['title'] == 'Joker')
