import unittest
from fulltmdb import find


class FindTest(unittest.TestCase):
    def test_find_by_id(self):
        result = find.find_by_id('tt7286456', external_source="imdb_id")
        self.assertTrue('movie_results' in result)
        self.assertTrue(result['movie_results'][0]['title'] == 'Joker')
