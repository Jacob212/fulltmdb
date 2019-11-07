from ..base import _call, _get_read_access_token

'''
All api requests under the keywords tab in https://developers.themoviedb.org/3/keywords
'''

def details(keyword_id):
    '''
    Gets name and id of keyword

    required: keyword_id 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/keyword/{keyword_id}', headers=headers)

def movies(keyword_id, **kwargs):
    '''
    Get the movies that belong to a keyword.
    We highly recommend using https://developers.themoviedb.org/3/discover/movie-discover instead of this method as it is much more flexible.

    required: keyword_id 
    optional:   language, include_adult
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/keyword/{keyword_id}/movies', params=kwargs, headers=headers)
