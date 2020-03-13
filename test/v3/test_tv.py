import unittest
from fulltmdb import tv

session_id = "15d84fae5caeee1086841399cc6deff8b2495f89"

class TvTest(unittest.TestCase):
    def test_details(self):
        result = tv.details(1399)
        self.assertTrue(result['name'] == 'Game of Thrones')

    def test_account_states(self):
        result = tv.account_states(1399, session_id=session_id)
        self.assertTrue('rated' in result)

    def test_alternative_titles(self):
        result = tv.alternative_titles(1399)
        self.assertTrue('results' in result)

    def test_changes(self):
        result = tv.changes(1399)
        self.assertTrue('changes' in result)

    def test_content_ratings(self):
        result = tv.content_ratings(1399)
        self.assertTrue('results' in result)

    def test_credits(self):
        result = tv.credits(1399)
        self.assertTrue('cast' in result)

    def test_episode_groups(self):
        result = tv.episode_groups(1399)
        self.assertTrue('results' in result)

    def test_external_ids(self):
        result = tv.external_ids(1399)
        self.assertTrue('id' in result)

    def test_images(self):
        result = tv.images(1399)
        self.assertTrue('backdrops' in result)

    def test_keywords(self):
        result = tv.keywords(1399)
        self.assertTrue('results' in result)

    def test_recommendations(self):
        result = tv.recommendations(1399)
        self.assertTrue('results' in result)

    def test_reviews(self):
        result = tv.reviews(1399)
        self.assertTrue('results' in result)

    def test_screened_theatrically(self):
        result = tv.screened_theatrically(1399)
        self.assertTrue('results' in result)

    def test_similar(self):
        result = tv.similar(1399)
        self.assertTrue('results' in result)

    def test_translations(self):
        result = tv.translations(1399)
        self.assertTrue('translations' in result)

    def test_videos(self):
        result = tv.videos(1399)
        self.assertTrue('results' in result)

    def test_rate_movie(self):
        result = tv.rate_movie(1399, 9, session_id=session_id)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)

    def test_1delete_rating(self):
        result = tv.delete_rating(1399, session_id=session_id)
        self.assertTrue(result['status_code'] == 13)

    def test_latest(self):
        result = tv.latest()
        self.assertTrue('id' in result)

    def test_airing_today(self):
        result = tv.airing_today()
        self.assertTrue('results' in result)

    def test_on_the_air(self):
        result = tv.on_the_air()
        self.assertTrue('results' in result)

    def test_popular(self):
        result = tv.popular()
        self.assertTrue('results' in result)

    def test_top_rated(self):
        result = tv.top_rated()
        self.assertTrue('results' in result)
