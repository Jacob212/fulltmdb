import unittest
from fulltmdb import Certifications


class CertificationsTest(unittest.TestCase):
    def test_movie(self):
        result = Certifications.movie()
        self.assertTrue('certifications' in result)

    def test_tv(self):
        result = Certifications.tv()
        self.assertTrue('certifications' in result)
