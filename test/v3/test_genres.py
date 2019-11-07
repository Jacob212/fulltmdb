import unittest
from fulltmdb import genres


class GenresTest(unittest.TestCase):
    def test_movie(self):
        result = genres.movie()
        self.assertTrue('genres' in result)

    def test_tv(self):
        result = genres.tv()
        self.assertTrue('genres' in result)
