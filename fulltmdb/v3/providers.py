from ..base import _call

'''
All api requests under the watch providers tab in https://developers.themoviedb.org/3/watch-providers
'''

def available_regions(disable_cache=False, **kwargs):
    '''
    Returns a list of all of the countries we have watch provider (OTT/streaming) data for.

    required: 
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/watch/providers/regions', disable_cache, params=kwargs)

def movie_providers(disable_cache=False, **kwargs):
    '''
    Returns a list of the watch provider (OTT/streaming) data we have available for movies.
    You can specify a watch_region param if you want to further filter the list by country.

    required: 
    optional: language, watch_region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/watch/providers/movie', disable_cache, params=kwargs)

def tv_providers(disable_cache=False, **kwargs):
    '''
    Returns a list of the watch provider (OTT/streaming) data we have available for TV series.
    You can specify a watch_region param if you want to further filter the list by country.

    required: 
    optional: language, watch_region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/watch/providers/tv', disable_cache, params=kwargs)