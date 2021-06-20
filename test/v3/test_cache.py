import unittest
import time
from fulltmdb import Setup, changes

Setup.set_cache(3600)


class CacheTest(unittest.TestCase):
    def test_cache(self):
        changes.movie()
        now = time.time()
        for i in range(50):
            changes.movie()
        total = time.time()-now
        now = time.time()
        for i in range(50):
            changes.movie(disable_cache=True)
        total2 = time.time()-now
        now = time.time()
        for i in range(50):
            changes.movie()
        total3 = time.time()-now
        now = time.time()
        for i in range(50):
            changes.movie(disable_cache=True)
        total4 = time.time()-now
        self.assertTrue(total2-1>total)
        self.assertTrue(total4-1>total3)
