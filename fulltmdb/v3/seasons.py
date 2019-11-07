from ..base import _call, _get_read_access_token

'''
All api requests under the tv seasons tab in https://developers.themoviedb.org/3/tv-seasons
'''


def details(tv_id, season_number, **kwargs):
    '''
    Get the TV season details by id.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: tv_id, season_number
    optional: language, append_to_response
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}', params=kwargs, headers=headers)


def changes(season_id, **kwargs):
    '''
    Get the changes for a TV season. By default only the last 24 hours are returned.

    You can query up to 14 days in a single query by using the start_date and end_date query parameters.

    required: season_id
    optional: page, start_date, end_date
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/season/{season_id}/changes', params=kwargs, headers=headers)


def account_states(tv_id, season_number, **kwargs):
    '''
    Returns all of the user ratings for the season's episodes.

    required: tv_id, season_number, session_id or guest_session_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/account_states', params=kwargs, headers=headers)


def credits(tv_id, season_number, **kwargs):
    '''
    Get the credits (cast and crew) that have been added to a TV show.

    required: tv_id, season_number
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/credits', params=kwargs, headers=headers)


def external_ids(tv_id, season_number, **kwargs):
    '''
    Get the external ids for a TV season. We currently support the following external sources.

    Media Databases
        TVDB ID
        Freebase MID*
        Freebase ID*
        TVRage ID*

    *Defunct or no longer available as a service.

    required: tv_id, season_number
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/external_ids', params=kwargs, headers=headers)


def images(tv_id, season_number, **kwargs):
    '''
    Get the images that belong to a TV season.
    Querying images with a language parameter will filter the results.
    If you want to include a fallback language (especially useful for backdrops) you can use the include_image_language parameter.
    This should be a comma seperated value like so: include_image_language=en,null.

    required: tv_id, season_number
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/images', params=kwargs, headers=headers)


def videos(tv_id, season_number, **kwargs):
    '''
    Get the videos that have been added to a TV season.

    required: tv_id, season_number
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/videos', params=kwargs, headers=headers)
