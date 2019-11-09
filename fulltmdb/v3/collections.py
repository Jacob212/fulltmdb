from ..base import _call
'''
All api requests under the collections tab in https://developers.themoviedb.org/3/collections
'''

def details(collection_id, **kwargs):
    '''
    Get collection details by id.

    required: collection_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}', params=kwargs)

def images(collection_id, **kwargs):
    '''
    Get the images for a collection by id.

    required: collection_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}/images', params=kwargs)

def translations(collection_id, **kwargs):
    '''
    Get the list translations for a collection by id.

    required: collection_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}/translations', params=kwargs)
