import unittest
from fulltmdb import Setup, changes

Setup.set_cache(3600)

class CacheTest(unittest.TestCase):
    def test_cache(self):
        Setup.just_json(False)
        result = changes.movie()
        self.assertTrue(result.from_cache is True)
        result = changes.movie(disable_cache=True)
        self.assertFalse(hasattr(result, 'from_cache'))
        Setup.just_json(True)