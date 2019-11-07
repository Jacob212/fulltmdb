import unittest
from fulltmdb import genres


class GenresTest(unittest.TestCase):
    def test_get_movie_list(self):
        result = genres.get_movie_list()
        self.assertTrue('genres' in result)

    def test_get_tv_list(self):
        result = genres.get_tv_list()
        self.assertTrue('genres' in result)
