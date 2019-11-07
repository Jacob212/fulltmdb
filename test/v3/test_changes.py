import unittest
from fulltmdb import changes


class ChangesTest(unittest.TestCase):
    def test_movie(self):
        result = changes.movie()
        self.assertTrue('results' in result)

    def test_tv(self):
        result = changes.tv()
        self.assertTrue('results' in result)

    def test_person(self):
        result = changes.person()
        self.assertTrue('results' in result)
