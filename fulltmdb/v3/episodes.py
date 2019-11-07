from ..base import _call, _get_read_access_token

'''
All api requests under the tv episodes tab in https://developers.themoviedb.org/3/tv-episodes
'''

def details(tv_id, season_number, episode_number, **kwargs):
    '''
    Get the TV episode details by id.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: tv_id, season_number, episode_number
    optional: language, append_to_response
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}', params=kwargs, headers=headers)

def changes(episode_id, **kwargs):
    '''
    Get the changes for a TV episode. By default only the last 24 hours are returned.
    You can query up to 14 days in a single query by using the start_date and end_date query parameters.

    required: episode_id
    optional: page, start_date, end_date
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/episode/{episode_id}/changes', params=kwargs, headers=headers)

def account_states(tv_id, season_number, episode_number, **kwargs):
    '''
    Get your rating for a episode.

    required: tv_id, season_number, episode_number, session_id or guest_session_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/account_states', params=kwargs, headers=headers)

def credits(tv_id, season_number, episode_number, **kwargs):
    '''
    Get the credits (cast, crew and guest stars) for a TV episode.

    required: tv_id, season_number, episode_number
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/credits', params=kwargs, headers=headers)

def external_ids(tv_id, season_number, episode_number, **kwargs):
    '''
    Get the external ids for a TV episode. We currently support the following external sources.

    Media Databases
        IMDB ID
        TVDB ID
        Freebase MID*
        Freebase ID*
        TVRage ID*

    *Defunct or no longer available as a service.

    required: tv_id, season_number, episode_number
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/external_ids', params=kwargs, headers=headers)

def images(tv_id, season_number, episode_number):
    '''
    Get the images that belong to a TV episode.
    Querying images with a language parameter will filter the results.
    If you want to include a fallback language (especially useful for backdrops) you can use the include_image_language parameter.
    This should be a comma seperated value like so: include_image_language=en,null.

    required: tv_id, season_number, episode_number
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/images', headers=headers)

def translations(tv_id, season_number, episode_number):
    '''
    Get the videos that have been added to a TV episode.

    required: tv_id, season_number, episode_number
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/translations', headers=headers)

def rate_episode(tv_id, season_number, episode_number, payload, **kwargs):
    '''
    Rate a TV episode.

    A valid session or guest session ID is required. You can read more about how this works https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

    required: tv_id, season_number, episode_number, session_id or guest_session_id
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating', params=kwargs, headers=headers, payload=payload)

def delete_rating(tv_id, season_number, episode_number, **kwargs):
    '''
    Remove your rating for a TV episode.

    A valid session or guest session ID is required. You can read more about how this works https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

    required: tv_id, season_number, episode_number, session_id or guest_session_id
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating', params=kwargs, headers=headers)

def videos(tv_id, season_number, episode_number, **kwargs):
    '''
    Get the videos that have been added to a TV episode.

    required: tv_id, season_number, episode_number
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/videos', params=kwargs, headers=headers)
