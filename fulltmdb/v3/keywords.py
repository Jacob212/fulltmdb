from ..base import _call, _headers

'''
All api requests under the keywords tab in https://developers.themoviedb.org/3/keywords
'''

def details(keyword_id):
    '''
    Gets name and id of keyword

    required: keyword_id 
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/keyword/{keyword_id}', headers=_headers)

def movies(keyword_id, **kwargs):
    '''
    Get the movies that belong to a keyword.
    We highly recommend using https://developers.themoviedb.org/3/discover/movie-discover instead of this method as it is much more flexible.

    required: keyword_id 
    optional:   language, include_adult
    '''

    return _call('GET', f'https://api.themoviedb.org/3/keyword/{keyword_id}/movies', params=kwargs, headers=_headers)
