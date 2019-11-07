from ..base import _call, _get_read_access_token

'''
All api requests under the account tab in https://developers.themoviedb.org/4/account
'''

def lists(account_id, **kwargs):
    '''
    Get all of the lists you've created.

    required: account_id 
    optional: page
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/lists', params=kwargs, headers=headers)

def favorite_movies(account_id, **kwargs):
    '''
    Get the list of movies you have marked as a favorite.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/movie/favorites', params=kwargs, headers=headers)

def favorite_tv(account_id, **kwargs):
    '''
    Get the list of TV shows you have marked as a favorite.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/tv/favorites', params=kwargs, headers=headers)

def movie_recommendations(account_id, **kwargs):
    '''
    Get a list of your personal movie recommendations.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/movie/recommendations', params=kwargs, headers=headers)

def tv_recommendations(account_id, **kwargs):
    '''
    Get a list of your personal TV show recommendations.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/tv/recommendations', params=kwargs, headers=headers)

def movie_watchlist(account_id, **kwargs):
    '''
    Get the list of movies you have added to your watchlist.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/movie/watchlist', params=kwargs, headers=headers)

def tv_watchlist(account_id, **kwargs):
    '''
    Get the list of TV shows you have added to your watchlist.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/tv/watchlist', params=kwargs, headers=headers)

def rated_movies(account_id, **kwargs):
    '''
    Get the list of movies you have rated.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/movie/rated', params=kwargs, headers=headers)

def rated_tv(account_id, **kwargs):
    '''
    Get the list of TV shows you have rated.

    required: account_id
    optional: page, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/account/{account_id}/tv/rated', params=kwargs, headers=headers)
