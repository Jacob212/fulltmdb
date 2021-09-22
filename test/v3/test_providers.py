import unittest
from fulltmdb import Providers


class ProvidersTest(unittest.TestCase):
    def test_available_regions(self):
        result = Providers.available_regions()
        self.assertTrue('results' in result)

    def test_movie_providers(self):
        result = Providers.movie_providers()
        self.assertTrue('results' in result)

    def test_tv_providers(self):
        result = Providers.tv_providers()
        self.assertTrue('results' in result)