import unittest
from fulltmdb import Setup, Changes

Setup.set_cache(3600)
Setup.clear_cache()

class CacheTest(unittest.TestCase):
    def test_cache(self):
        Setup.just_json(False)
        result = Changes.movie()
        result = Changes.movie()
        result2 = Changes.movie(disable_cache=True)
        Setup.just_json(True)
        self.assertTrue(hasattr(result, 'from_cache'))
        self.assertTrue(str(result.from_cache) == 'True')
        self.assertFalse(hasattr(result2, 'from_cache'))