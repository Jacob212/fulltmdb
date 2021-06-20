from ..base import _call
'''
All api requests under the collections tab in https://developers.themoviedb.org/3/collections
'''

def details(collection_id, disable_cache=False, **kwargs):
    '''
    Get collection details by id.

    required: collection_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}', disable_cache, params=kwargs)

def images(collection_id, disable_cache=False, **kwargs):
    '''
    Get the images for a collection by id.

    required: collection_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}/images', disable_cache, params=kwargs)

def translations(collection_id, disable_cache=False, **kwargs):
    '''
    Get the list translations for a collection by id.

    required: collection_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}/translations', disable_cache, params=kwargs)
