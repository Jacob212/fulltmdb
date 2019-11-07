from ..base import _call, _get_read_access_token

'''
All api requests under the genres tab in https://developers.themoviedb.org/3/genres
'''

def movie(**kwargs):
    '''
    Get the list of official genres for movies.

    required: 
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/genre/movie/list', params=kwargs, headers=headers)

def tv(**kwargs):
    '''
    Get the list of official genres for TV shows.

    required: 
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/genre/tv/list', params=kwargs, headers=headers)
