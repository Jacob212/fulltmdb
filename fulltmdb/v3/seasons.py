from ..base import _call

'''
All api requests under the tv seasons tab in https://developers.themoviedb.org/3/tv-seasons
'''


def details(tv_id, season_number, disable_cache=False, **kwargs):
    '''
    Get the TV season details by id.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: tv_id, season_number
    optional: language, append_to_response
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}', disable_cache, params=kwargs)


def changes(season_id, disable_cache=False, **kwargs):
    '''
    Get the changes for a TV season. By default only the last 24 hours are returned.

    You can query up to 14 days in a single query by using the start_date and end_date query parameters.

    required: season_id
    optional: page, start_date, end_date
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/season/{season_id}/changes', disable_cache, params=kwargs)


def account_states(tv_id, season_number, disable_cache=False, **kwargs):
    '''
    Returns all of the user ratings for the season's episodes.

    required: tv_id, season_number, session_id or guest_session_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/account_states', disable_cache, params=kwargs)


def credits(tv_id, season_number, disable_cache=False, **kwargs):
    '''
    Get the credits (cast and crew) that have been added to a TV show.

    required: tv_id, season_number
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/credits', disable_cache, params=kwargs)


def external_ids(tv_id, season_number, disable_cache=False, **kwargs):
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

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/external_ids', disable_cache, params=kwargs)


def images(tv_id, season_number, disable_cache=False, **kwargs):
    '''
    Get the images that belong to a TV season.
    Querying images with a language parameter will filter the results.
    If you want to include a fallback language (especially useful for backdrops) you can use the include_image_language parameter.
    This should be a comma seperated value like so: include_image_language=en,null.

    required: tv_id, season_number
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/images', disable_cache, params=kwargs)


def videos(tv_id, season_number, disable_cache=False, **kwargs):
    '''
    Get the videos that have been added to a TV season.

    required: tv_id, season_number
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/videos', disable_cache, params=kwargs)
