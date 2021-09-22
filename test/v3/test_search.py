import unittest
from fulltmdb import Search


class SearchTest(unittest.TestCase):
    def test_companies(self):
        result = Search.companies(query='Netflix')
        self.assertTrue('results' in result)

    def test_collections(self):
        result = Search.collections(query='Harry Potter')
        self.assertTrue('results' in result)

    def test_keywords(self):
        result = Search.keywords(query='war')
        self.assertTrue('results' in result)

    def test_movies(self):
        result = Search.movies(query='Superman')
        self.assertTrue('results' in result)

    def test_multi(self):
        result = Search.multi(query='The Flash')
        self.assertTrue('results' in result)

    def test_people(self):
        result = Search.people(query='Brad Pitt')
        self.assertTrue('results' in result)

    def test_tv(self):
        result = Search.tv(query='Game of Thrones')
        self.assertTrue('results' in result)
