from ..base import _call, _get_read_access_token

'''
All api requests under the guest sessions tab in https://developers.themoviedb.org/3/guest-sessions
'''

def rated_movies(guest_session_id, **kwargs):
    '''
    Get the rated movies for a guest session.

    required: guest_session_id
    optional: language, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/movies', params=kwargs, headers=headers)

def rated_tv_shows(guest_session_id, **kwargs):
    '''
    Get the rated TV shows for a guest session.

    required: guest_session_id
    optional: language, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/tv', params=kwargs, headers=headers)

def rated_tv_episodes(guest_session_id, **kwargs):
    '''
    Get the rated TV episodes for a guest session.

    required: guest_session_id
    optional: language, sort_by
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/tv/episodes', params=kwargs, headers=headers)
