from ..base import _call, _get_read_access_token
'''
All api requests under the collections tab in https://developers.themoviedb.org/3/collections
'''

def get_details(collection_id, **kwargs):
    '''
    Get collection details by id.

    required: collection_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}', params=kwargs, headers=headers)

def get_images(collection_id, **kwargs):
    '''
    Get the images for a collection by id.

    required: collection_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}/images', params=kwargs, headers=headers)

def get_translations(collection_id, **kwargs):
    '''
    Get the list translations for a collection by id.

    required: collection_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/collection/{collection_id}/translations', params=kwargs, headers=headers)
