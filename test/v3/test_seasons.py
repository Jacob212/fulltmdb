import unittest
from fulltmdb import seasons

session_id = "15d84fae5caeee1086841399cc6deff8b2495f89"

class SeasonsTest(unittest.TestCase):
    def test_details(self):
        result = seasons.details(3624, 1)
        self.assertTrue('name' in result)

    def test_changes(self):
        result = seasons.changes('5256c89f19c2956ff6046d47')
        self.assertTrue('changes' in result)

    def test_account_states(self):
        result = seasons.account_states(3624, 1, session_id=session_id)
        self.assertTrue('results' in result)

    def test_credits(self):
        result = seasons.credits(3624, 1)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = seasons.external_ids(3624, 1)
        self.assertTrue('id' in result)

    def test_images(self):
        result = seasons.images(3624, 1)
        self.assertTrue('posters' in result)

    def test_videos(self):
        result = seasons.videos(3624, 1)
        self.assertTrue('results' in result)
