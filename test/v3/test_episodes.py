import unittest
from fulltmdb import episodes


class EpisodesTest(unittest.TestCase):
    def test_details(self):
        result = episodes.details(1399,1,1)
        self.assertTrue('air_date' in result)

    def test_changes(self):
        result = episodes.changes(10)
        self.assertTrue('changes' in result)

    # def test_account_states(self): session_id needed
    #     result = episodes.account_states()
    #     self.assertTrue('changes' in result)

    def test_credits(self):
        result = episodes.credits(1399,1,1)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = episodes.external_ids(1399,1,1)
        self.assertTrue('imdb_id' in result)

    def test_images(self):
        result = episodes.images(1399,1,1)
        self.assertTrue('stills' in result)

    def test_translations(self):
        result = episodes.translations(1399,1,1)
        self.assertTrue('translations' in result)

    # def test_rate_episode(self): session_id needed
    #     result = episodes.rate_episode(1399,1,1)
    #     self.assertTrue('changes' in result)

    # def test_delete_rating(self): session_id needed
    #     result = episodes.delete_rating(1399,1,1)
    #     self.assertTrue('changes' in result)

    def test_videos(self):
        result = episodes.videos(1399,1,1)
        self.assertTrue('results' in result)
