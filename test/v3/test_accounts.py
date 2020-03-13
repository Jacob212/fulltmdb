import unittest
from fulltmdb import accounts

session_id = "15d84fae5caeee1086841399cc6deff8b2495f89"
account_id = 8399416

class AccountsTest(unittest.TestCase):
    def test_details(self):
        result = accounts.details(session_id)
        self.assertTrue('username' in result)

    def test_created_lists(self):
        result = accounts.created_lists(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_favorite_movies(self):
        result = accounts.favorite_movies(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_favorite_tv_shows(self):
        result = accounts.favorite_tv_shows(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_mark_as_favorite(self):
        result = accounts.mark_as_favorite(account_id, session_id, "movie", 550, True)
        self.assertTrue(result['status_code'] == 12)
        result = accounts.mark_as_favorite(account_id, session_id, "movie", 550, False)
        self.assertTrue(result['status_code'] == 12)

    def test_rated_movies(self):
        result = accounts.rated_movies(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_rated_tv(self):
        result = accounts.rated_tv(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_rated_tv_episodes(self):
        result = accounts.rated_tv_episodes(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_movie_watchlist(self):
        result = accounts.rated_tv_episodes(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_tv_show_watchlist(self):
        result = accounts.tv_show_watchlist(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_add_to_watchlist(self):
        result = accounts.add_to_watchlist(account_id, session_id, "movie", 550, True)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)#whats going on here???? different status codes for same response
        result = accounts.add_to_watchlist(account_id, session_id, "movie", 550, False)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)