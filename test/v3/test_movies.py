import unittest
from os import environ
from fulltmdb import Movies

session_id = environ.get('SESSION_ID')

class MoviesTest(unittest.TestCase):
    def test_details(self):
        result = Movies.details(550)
        self.assertTrue(result['original_title'] == "Fight Club")

    def test_account_states(self):
        result = Movies.account_states(550, session_id=session_id)
        self.assertTrue('rated' in result)

    def test_alternative_titles(self):
        result = Movies.alternative_titles(550)
        self.assertTrue('titles' in result)

    def test_changes(self):
        result = Movies.changes(550)
        self.assertTrue('changes' in result)

    def test_credits(self):
        result = Movies.credits(550)
        self.assertTrue('cast' in result)

    def test_external_ids(self):
        result = Movies.external_ids(550)
        self.assertTrue('id' in result)

    def test_images(self):
        result = Movies.images(550)
        self.assertTrue('backdrops' in result)

    def test_keywords(self):
        result = Movies.keywords(550)
        self.assertTrue('keywords' in result)

    def test_release_dates(self):
        result = Movies.release_dates(550)
        self.assertTrue('results' in result)

    def test_videos(self):
        result = Movies.videos(550)
        self.assertTrue('results' in result)

    def test_translations(self):
        result = Movies.translations(550)
        self.assertTrue('translations' in result)

    def test_recommendations(self):
        result = Movies.recommendations(550)
        self.assertTrue('results' in result)

    def test_similar(self):
        result = Movies.similar(550)
        self.assertTrue('results' in result)

    def test_reviews(self):
        result = Movies.reviews(550)
        self.assertTrue('results' in result)

    def test_lists(self):
        result = Movies.lists(550)
        self.assertTrue('results' in result)

    def test_rate_movie(self):
        result = Movies.rate_movie(550, 9, session_id=session_id)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)

    def test_1delete_rating(self):
        result = Movies.delete_rating(550, session_id=session_id)
        self.assertTrue(result['status_code'] == 13)

    def test_latest(self):
        result = Movies.latest()
        self.assertTrue('id' in result)

    def test_now_playing(self):
        result = Movies.now_playing()
        self.assertTrue('results' in result)

    def test_popular(self):
        result = Movies.popular()
        self.assertTrue('results' in result)

    def test_top_rated(self):
        result = Movies.top_rated()
        self.assertTrue('results' in result)

    def test_upcoming(self):
        result = Movies.upcoming()
        self.assertTrue('results' in result)
