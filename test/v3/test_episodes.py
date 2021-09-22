import unittest
from os import environ
from fulltmdb import Episodes

session_id = environ.get('SESSION_ID')

class EpisodesTest(unittest.TestCase):
    def test_details(self):
        result = Episodes.details(1399, 1, 1)
        self.assertTrue('air_date' in result)

    def test_changes(self):
        result = Episodes.changes(10)
        self.assertTrue('changes' in result)

    def test_account_states(self):
        result = Episodes.account_states(1399, 1, 1, session_id=session_id)
        self.assertTrue('rated' in result)

    def test_credits(self):
        result = Episodes.credits(1399, 1, 1)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = Episodes.external_ids(1399, 1, 1)
        self.assertTrue('imdb_id' in result)

    def test_images(self):
        result = Episodes.images(1399, 1, 1)
        self.assertTrue('stills' in result)

    def test_translations(self):
        result = Episodes.translations(1399, 1, 1)
        self.assertTrue('translations' in result)

    def test_rate_episode(self):
        result = Episodes.rate_episode(1399, 1, 1, 9, session_id=session_id)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)

    def test_delete_rating(self):
        result = Episodes.delete_rating(1399, 1, 1, session_id=session_id)
        self.assertTrue(result['status_code'] == 13)

    def test_videos(self):
        result = Episodes.videos(1399, 1, 1)
        self.assertTrue('results' in result)
