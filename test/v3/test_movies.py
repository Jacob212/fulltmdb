import unittest
from fulltmdb import movies


class MoviesTest(unittest.TestCase):
    def test_details(self):
        result = movies.details(550)
        self.assertTrue(result['original_title'] == "Fight Club")

    # def test_account_states(self): session_id needed
    #     result = movies.account_states()
    #     self.assertTrue('changes' in result)

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
        result = movies.translations(550)
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
