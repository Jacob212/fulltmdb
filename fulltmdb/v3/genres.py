from ..base import _call

'''
All api requests under the genres tab in https://developers.themoviedb.org/3/genres
'''

def movie(disable_cache=False, **kwargs):
    '''
    Get the list of official genres for movies.

    required: 
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/genre/movie/list', disable_cache, params=kwargs)

def tv(disable_cache=False, **kwargs):
    '''
    Get the list of official genres for TV shows.

    required: 
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/genre/tv/list', disable_cache, params=kwargs)
