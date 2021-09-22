import unittest
from fulltmdb import Changes


class ChangesTest(unittest.TestCase):
    def test_movie(self):
        result = Changes.movie()
        self.assertTrue('results' in result)

    def test_tv(self):
        result = Changes.tv()
        self.assertTrue('results' in result)

    def test_person(self):
        result = Changes.person()
        self.assertTrue('results' in result)
