from ..base import _call, _get_read_access_token

'''
All api requests under the search tab in https://developers.themoviedb.org/3/search
'''

def companies(**kwargs):
    '''
    Search for companies.

    required: query
    optional: page
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/search/company', params=kwargs, headers=headers)

def collections(**kwargs):
    '''
    Search for collections.

    required: query
    optional: page, language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/search/collection', params=kwargs, headers=headers)

def keywords(**kwargs):
    '''
    Search for keywords.

    required: query
    optional: page
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/search/keyword', params=kwargs, headers=headers)

def movies(**kwargs):
    '''
    Search for movies.

    required: query
    optional: page, language, include_adult, region, year, primary_release_year
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/search/movie', params=kwargs, headers=headers)

def multi(**kwargs):
    '''
    Search multiple models in a single request.
    Multi search currently supports searching for movies, tv shows and people in a single request.

    required: query
    optional: page, language, include_adult, region
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/search/multi', params=kwargs, headers=headers)

def people(**kwargs):
    '''
    Search for people.

    required: query
    optional: page, language, include_adult, region
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/search/person', params=kwargs, headers=headers)

def tv(**kwargs):
    '''
    Search for a TV show.

    required: query
    optional: page, language, first_air_date_year
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/search/tv', params=kwargs, headers=headers)
