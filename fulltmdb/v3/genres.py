from ..base import _call

'''
All api requests under the genres tab in https://developers.themoviedb.org/3/genres
'''

def movie(**kwargs):
    '''
    Get the list of official genres for movies.

    required: 
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/genre/movie/list', params=kwargs)

def tv(**kwargs):
    '''
    Get the list of official genres for TV shows.

    required: 
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/genre/tv/list', params=kwargs)
