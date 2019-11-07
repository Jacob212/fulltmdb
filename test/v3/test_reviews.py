import unittest
from fulltmdb import reviews


class ReviewsTest(unittest.TestCase):
    def test_get_details(self):
        result = reviews.get_details('5488c29bc3a3686f4a00004a')
        self.assertTrue('author' in result)
