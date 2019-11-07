import unittest
from fulltmdb import certifications

class CertificationsTest(unittest.TestCase):
    def test_get_movie_certifications(self):
        result = certifications.get_movie_certifications()
        self.assertTrue('certifications' in result)

    def test_get_tv_certifications(self):
        result = certifications.get_tv_certifications()
        self.assertTrue('certifications' in result)
