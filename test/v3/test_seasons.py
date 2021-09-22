import unittest
from os import environ
from fulltmdb import Seasons

session_id = environ.get('SESSION_ID')

class SeasonsTest(unittest.TestCase):
    def test_details(self):
        result = Seasons.details(3624, 1)
        self.assertTrue('name' in result)

    def test_changes(self):
        result = Seasons.changes('5256c89f19c2956ff6046d47')
        self.assertTrue('changes' in result)

    def test_account_states(self):
        result = Seasons.account_states(3624, 1, session_id=session_id)
        self.assertTrue('results' in result)

    def test_credits(self):
        result = Seasons.credits(3624, 1)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = Seasons.external_ids(3624, 1)
        self.assertTrue('id' in result)

    def test_images(self):
        result = Seasons.images(3624, 1)
        self.assertTrue('posters' in result)

    def test_videos(self):
        result = Seasons.videos(3624, 1)
        self.assertTrue('results' in result)
