from ..base import _call

'''
All api requests under the search tab in https://developers.themoviedb.org/3/search
'''

def companies(disable_cache=False, **kwargs):
    '''
    Search for companies.

    required: query
    optional: page
    '''

    return _call('GET', f'https://api.themoviedb.org/3/search/company', disable_cache, params=kwargs)

def collections(disable_cache=False, **kwargs):
    '''
    Search for collections.

    required: query
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/search/collection', disable_cache, params=kwargs)

def keywords(disable_cache=False, **kwargs):
    '''
    Search for keywords.

    required: query
    optional: page
    '''

    return _call('GET', f'https://api.themoviedb.org/3/search/keyword', disable_cache, params=kwargs)

def movies(disable_cache=False, **kwargs):
    '''
    Search for movies.

    required: query
    optional: page, language, include_adult, region, year, primary_release_year
    '''

    return _call('GET', f'https://api.themoviedb.org/3/search/movie', disable_cache, params=kwargs)

def multi(disable_cache=False, **kwargs):
    '''
    Search multiple models in a single request.
    Multi search currently supports searching for movies, tv shows and people in a single request.

    required: query
    optional: page, language, include_adult, region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/search/multi', disable_cache, params=kwargs)

def people(disable_cache=False, **kwargs):
    '''
    Search for people.

    required: query
    optional: page, language, include_adult, region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/search/person', disable_cache, params=kwargs)

def tv(disable_cache=False, **kwargs):
    '''
    Search for a TV show.

    required: query
    optional: page, language, first_air_date_year
    '''

    return _call('GET', f'https://api.themoviedb.org/3/search/tv', disable_cache, params=kwargs)
