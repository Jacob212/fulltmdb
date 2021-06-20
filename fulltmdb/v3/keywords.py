from ..base import _call

'''
All api requests under the keywords tab in https://developers.themoviedb.org/3/keywords
'''


def details(keyword_id, disable_cache=False):
    '''
    Gets name and id of keyword

    required: keyword_id
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/keyword/{keyword_id}', disable_cache)


def movies(keyword_id, disable_cache=False, **kwargs):
    '''
    Get the movies that belong to a keyword.
    We highly recommend using https://developers.themoviedb.org/3/discover/movie-discover instead of this method as it is much more flexible.

    required: keyword_id
    optional:   language, include_adult
    '''

    return _call('GET', f'https://api.themoviedb.org/3/keyword/{keyword_id}/movies', disable_cache, params=kwargs)
