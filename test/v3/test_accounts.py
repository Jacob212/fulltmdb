import unittest
from os import environ
from fulltmdb import Accounts

session_id = environ.get('SESSION_ID')
account_id = environ.get('ACCOUNT_ID')

class AccountsTest(unittest.TestCase):
    def test_details(self):
        result = Accounts.details(session_id)
        self.assertTrue('username' in result)

    def test_created_lists(self):
        result = Accounts.created_lists(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_favorite_movies(self):
        result = Accounts.favorite_movies(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_favorite_tv_shows(self):
        result = Accounts.favorite_tv_shows(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_mark_as_favorite(self):
        result = Accounts.mark_as_favorite(account_id, session_id, "movie", 550, True)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)#whats going on here???? different status codes for same response
        result = Accounts.mark_as_favorite(account_id, session_id, "movie", 550, False)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)#whats going on here???? different status codes for same response

    def test_rated_movies(self):
        result = Accounts.rated_movies(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_rated_tv(self):
        result = Accounts.rated_tv(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_rated_tv_episodes(self):
        result = Accounts.rated_tv_episodes(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_movie_watchlist(self):
        result = Accounts.rated_tv_episodes(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_tv_show_watchlist(self):
        result = Accounts.tv_show_watchlist(account_id, session_id=session_id)
        self.assertTrue('results' in result)

    def test_add_to_watchlist(self):
        result = Accounts.add_to_watchlist(account_id, session_id, "movie", 550, True)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)#whats going on here???? different status codes for same response
        result = Accounts.add_to_watchlist(account_id, session_id, "movie", 550, False)
        self.assertTrue(result['status_code'] == 12 or result['status_code'] == 1)