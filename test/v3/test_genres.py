import unittest
from fulltmdb import Genres


class GenresTest(unittest.TestCase):
    def test_movie(self):
        result = Genres.movie()
        self.assertTrue('genres' in result)

    def test_tv(self):
        result = Genres.tv()
        self.assertTrue('genres' in result)
