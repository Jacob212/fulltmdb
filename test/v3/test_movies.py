import unittest
from os import environ
from fulltmdb import movies

session_id = environ['SESSION_ID']

class MoviesTest(unittest.TestCase):
    def test_details(self):
        result = movies.details(550)
        self.assertTrue(result['original_title'] == "Fight Club")

    def test_account_states(self):
        result = movies.account_states(550, session_id=session_id)
        self.assertTrue('rated' in result)

    def test_alternative_titles(self):
        result = movies.alternative_titles(550)
        self.assertTrue('titles' in result)

    def test_changes(self):
        result = movies.changes(550)
        self.assertTrue('changes' in result)

    def test_credits(self):
        result = movies.credits(550)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = movies.external_ids(550)
        self.assertTrue('id' in result)

    def test_images(self):
        result = movies.images(550)
        self.assertTrue('backdrops' in result)

    def test_keywords(self):
        result = movies.keywords(550)
        self.assertTrue('keywords' in result)

    def test_release_dates(self):
        result = movies.release_dates(550)
        self.assertTrue('results' in result)

    def test_videos(self):
        result = movies.videos(550)
        self.assertTrue('results' in result)

    def test_translations(self):
        result = movies.translations(550)
        self.assertTrue('translations' in result)

    def test_recommendations(self):
        result = movies.recommendations(550)
        self.assertTrue('results' in result)

    def test_similar(self):
        result = movies.similar(550)
        self.assertTrue('results' in result)

    def test_reviews(self):
        result = movies.reviews(550)
        self.assertTrue('results' in result)

    def test_lists(self):
        result = movies.lists(550)
        self.assertTrue('results' in result)

    def test_rate_movie(self):
        result = movies.rate_movie(550, 9, session_id=session_id)
        self.assertTrue(result['status_code'] == 1)

    def test_1delete_rating(self):
        result = movies.delete_rating(550, session_id=session_id)
        self.assertTrue(result['status_code'] == 13)

    def test_latest(self):
        result = movies.latest()
        self.assertTrue('id' in result)

    def test_now_playing(self):
        result = movies.now_playing()
        self.assertTrue('results' in result)

    def test_popular(self):
        result = movies.popular()
        self.assertTrue('results' in result)

    def test_top_rated(self):
        result = movies.top_rated()
        self.assertTrue('results' in result)

    def test_upcoming(self):
        result = movies.upcoming()
        self.assertTrue('results' in result)
