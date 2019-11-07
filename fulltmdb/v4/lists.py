from ..base import _call, _get_read_access_token

'''
All api requests under the list tab in https://developers.themoviedb.org/4/list
'''

def list(list_id, access_token, **kwargs):
    '''
    Get the details of a list.

    required: list_id
    optional: page, language, sort_by
    '''

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/list/{list_id}', params=kwargs, headers=headers)

def create_list(access_token, payload):
    '''
    This method will create a new list.
    You will need to have valid user access token in order to create a new list.

    required: payload 
    optional: 
    '''

    # payload = {
    #     "name": name,
    #     "iso_639_1": iso,
    #     'description': description,
    #     'public': public
    #     }

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/4/list', headers=headers, payload=payload)

def update_list(access_token, list_id, payload):
    '''
    This method will let you update the details of a list.
    You must be the owner of the list and therefore have a valid user access token in order to edit it.

    required: list_id, payload
    optional: 
    '''
    # payload = {
    #     'name': name,
    #     'description': description,
    #     'language': language
    #     }

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('PUT', f'https://api.themoviedb.org/4/list/{list_id}', headers=headers, payload=payload)

def clear_list(access_token, list_id):
    '''
    This method lets you clear all of the items from a list in a single request.
    This action cannot be reversed so use it with caution.
    You must be the owner of the list and therefore have a valid user access token in order to clear a list.

    required: list_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/4/list/{list_id}/clear', headers=headers)

def delete_list(access_token, list_id):
    '''
    This method will delete a list by id. This action is not reversible so take care when issuing it.
    You must be the owner of the list and therefore have a valid user access token in order to delete it.

    required: list_id, session_id, media_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('DELETE', f'https://api.themoviedb.org/4/list/{list_id}', headers=headers)

def add_items(access_token, list_id, payload):
    '''
    This method will let you add items to a list. We support essentially an unlimited number of items to be posted at a time.
    Both movie and TV series are support.

    The results of this query will return a results array.
    Each result includes a success field. If a result is false this will usually indicate that the item already exists on the list.
    It may also indicate that the item could not be found.

    You must be the owner of the list and therefore have a valid user access token in order to add items to a list.

    required: list_id, payload
    optional:
    '''

    # payload = {
    #     example payload
    # }

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/4/list/{list_id}/items', headers=headers, payload=payload)

def update_items(access_token, list_id, payload):
    '''
    This method will let you update an individual item on a list. Currently, only adding a comment is suported.

    You must be the owner of the list and therefore have a valid user access token in order to edit items.

    required: list_id, payload
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('PUT', f'https://api.themoviedb.org/4/list/{list_id}/items', headers=headers, payload=payload)

def remove_items(access_token, list_id, payload):
    '''
    This method will let you remove items from a list. You can remove multiple items at a time.

    You must be the owner of the list and therefore have a valid user access token in order to delete items from it.

    required: list_id, payload
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('DELETE', f'https://api.themoviedb.org/4/list/{list_id}/items', headers=headers, payload=payload)

def check_item_status(access_token, list_id, **kwargs):
    '''
    This method lets you quickly check if the item is already added to the list.

    You must be the owner of the list and therefore have a valid user access token in order to check an item status.

    required: list_id, media_id, media_type
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {access_token}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('DELETE', f'https://api.themoviedb.org/4/list/{list_id}/item_status', params=kwargs, headers=headers)