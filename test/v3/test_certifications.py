import unittest
from fulltmdb import certifications


class CertificationsTest(unittest.TestCase):
    def test_movie(self):
        result = certifications.movie()
        self.assertTrue('certifications' in result)

    def test_tv(self):
        result = certifications.tv()
        self.assertTrue('certifications' in result)
