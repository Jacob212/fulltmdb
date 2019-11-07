import unittest
from fulltmdb import reviews


class ReviewsTest(unittest.TestCase):
    def test_details(self):
        result = reviews.details('5488c29bc3a3686f4a00004a')
        self.assertTrue('author' in result)
