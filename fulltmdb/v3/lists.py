from ..base import _call, _get_read_access_token

'''
All api requests under the lists tab in https://developers.themoviedb.org/3/lists
'''

def details(list_id, **kwargs):
    '''
    Get the details of a list.

    required: list_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/list/{list_id}', params=kwargs, headers=headers)

def check_item_status(list_id, **kwargs):
    '''
    You can use this method to check if a movie has already been added to the list.

    required: list_id, movie_id
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/list/{list_id}/item_status', params=kwargs, headers=headers)

def create_list(session_id, name, description='', language='en'):
    '''
    Create a list.

    required: session_id, name
    optional: description, language
    '''
    payload = {
        'name': name,
        'description': description,
        'language': language
        }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/list?session_id={session_id}', headers=headers, payload=payload)

def add_movie(list_id, session_id, media_id):
    '''
    Add a movie to a list.

    required: list_id, session_id, media_id
    optional: 
    '''
    payload = {
        'media_id': media_id
        }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/list/{list_id}/add_item?session_id={session_id}', headers=headers, payload=payload)

def remove_movie(list_id, session_id, media_id):
    '''
    Remove a movie to a list.

    required: list_id, session_id, media_id
    optional: 
    '''
    payload = {
        'media_id': media_id
        }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/list/{list_id}/remove_item?session_id={session_id}', headers=headers, payload=payload)

def clear_list(list_id, session_id, confirm="true"):
    '''
    Clear a list.

    required: list_id, session_id, confirm
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/list/{list_id}/clear?session_id={session_id}&confirm={confirm}', headers=headers)

def delete_list(list_id, session_id):
    '''
    Delete a list.

    required: list_id, session_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('DELETE', f'https://api.themoviedb.org/3/list/{list_id}?session_id={session_id}', headers=headers)
