import unittest
from fulltmdb import search


class SearchTest(unittest.TestCase):
    def test_companies(self):
        result = search.companies(query='Netflix')
        self.assertTrue('results' in result)

    def test_collections(self):
        result = search.collections(query='Harry Potter')
        self.assertTrue('results' in result)

    def test_keywords(self):
        result = search.keywords(query='war')
        self.assertTrue('results' in result)

    def test_movies(self):
        result = search.movies(query='Superman')
        self.assertTrue('results' in result)

    def test_multi(self):
        result = search.multi(query='The Flash')
        self.assertTrue('results' in result)

    def test_people(self):
        result = search.people(query='Brad Pitt')
        self.assertTrue('results' in result)

    def test_tv(self):
        result = search.tv(query='Game of Thrones')
        self.assertTrue('results' in result)
