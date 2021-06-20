from ..base import _call

'''
All api requests under the guest sessions tab in https://developers.themoviedb.org/3/guest-sessions
'''

def rated_movies(guest_session_id, disable_cache=False, **kwargs):
    '''
    Get the rated movies for a guest session.

    required: guest_session_id
    optional: language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/movies', disable_cache, params=kwargs)

def rated_tv_shows(guest_session_id, disable_cache=False, **kwargs):
    '''
    Get the rated TV shows for a guest session.

    required: guest_session_id
    optional: language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/tv', disable_cache, params=kwargs)

def rated_tv_episodes(guest_session_id, disable_cache=False, **kwargs):
    '''
    Get the rated TV episodes for a guest session.

    required: guest_session_id
    optional: language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/tv/episodes', disable_cache, params=kwargs)
