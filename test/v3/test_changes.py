import unittest
from fulltmdb import changes

class ChangesTest(unittest.TestCase):
    def test_get_movie_change_list(self):
        result = changes.get_movie_change_list()
        self.assertTrue(hasattr(result, 'results'))

    def test_get_tv_change_list(self):
        result = changes.get_tv_change_list()
        self.assertTrue(hasattr(result, 'results'))

    def test_get_person_change_list(self):
        result = changes.get_person_change_list()
        self.assertTrue(hasattr(result, 'results'))
