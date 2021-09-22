import unittest
from os import environ
from fulltmdb import Tv

session_id = environ.get('SESSION_ID')

class TvTest(unittest.TestCase):
    def test_details(self):
        result = Tv.details(1399)
        self.assertTrue(result['name'] == 'Game of Thrones')

    def test_account_states(self):
        result = Tv.account_states(1399, session_id=session_id)
        self.assertTrue('rated' in result)

    def test_alternative_titles(self):
        result = Tv.alternative_titles(1399)
        self.assertTrue('results' in result)

    def test_changes(self):
        result = Tv.changes(1399)
        self.assertTrue('changes' in result)

    def test_content_ratings(self):
        result = Tv.content_ratings(1399)
        self.assertTrue('results' in result)

    def test_credits(self):
        result = Tv.credits(1399)
        self.assertTrue('cast' in result)

    def test_episode_groups(self):
        result = Tv.episode_groups(1399)
        self.assertTrue('results' in result)

    def test_external_ids(self):
        result = Tv.external_ids(1399)
        self.assertTrue('id' in result)

    def test_images(self):
        result = Tv.images(1399)
        self.assertTrue('backdrops' in result)

    def test_keywords(self):
        result = Tv.keywords(1399)
        self.assertTrue('results' in result)

    def test_recommendations(self):
        result = Tv.recommendations(1399)
        self.assertTrue('results' in result)

    def test_reviews(self):
        result = Tv.reviews(1399)
        self.assertTrue('results' in result)

    def test_screened_theatrically(self):
        result = Tv.screened_theatrically(1399)
        self.assertTrue('results' in result)

    def test_similar(self):
        result = Tv.similar(1399)
        self.assertTrue('results' in result)

    def test_translations(self):
        result = Tv.translations(1399)
        self.assertTrue('translations' in result)

    def test_videos(self):
        result = Tv.videos(1399)
        self.assertTrue('results' in result)

    def test_rate_movie(self):
        result = Tv.rate_movie(1399, 9, session_id=session_id)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)

    def test_1delete_rating(self):
        result = Tv.delete_rating(1399, session_id=session_id)
        self.assertTrue(result['status_code'] == 13)

    def test_latest(self):
        result = Tv.latest()
        self.assertTrue('id' in result)

    def test_airing_today(self):
        result = Tv.airing_today()
        self.assertTrue('results' in result)

    def test_on_the_air(self):
        result = Tv.on_the_air()
        self.assertTrue('results' in result)

    def test_popular(self):
        result = Tv.popular()
        self.assertTrue('results' in result)

    def test_top_rated(self):
        result = Tv.top_rated()
        self.assertTrue('results' in result)
