from ..base import _call

'''
All api requests under the tv tab in https://developers.themoviedb.org/3/tv
'''

def details(tv_id, disable_cache=False, **kwargs):
    '''
    Get the primary TV show details by id.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: tv_id
    optional: language, append_to_response
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}', disable_cache, params=kwargs)

def account_states(tv_id, disable_cache=False, **kwargs):
    '''
    Grab the following account states for a session:
        TV show rating
        If it belongs to your watchlist
        If it belongs to your favourite list

    required: tv_id, session_id or guest_session_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/account_states', disable_cache, params=kwargs)

def alternative_titles(tv_id, disable_cache=False, **kwargs):
    '''
    Returns all of the alternative titles for a TV show.

    required: tv_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/alternative_titles', disable_cache, params=kwargs)

def changes(tv_id, disable_cache=False, **kwargs):
    '''
    Get the changes for a TV show. By default only the last 24 hours are returned.
    You can query up to 14 days in a single query by using the start_date and end_date query parameters.

    TV show changes are different than movie changes in that there are some edits on seasons and episodes that will create a change entry at the show level.
    These can be found under the season and episode keys. These keys will contain a series_id and episode_id.
    You can use the https://developers.themoviedb.org/3/tv-seasons/get-tv-season-changes and https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-changes methods to look these up individually.

    required: tv_id
    optional: page, start_date, end_date
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/changes', disable_cache, params=kwargs)

def content_ratings(tv_id, disable_cache=False, **kwargs):
    '''
    Get the list of content ratings (certifications) that have been added to a TV show.

    required: tv_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/content_ratings', disable_cache, params=kwargs)

def credits(tv_id, disable_cache=False, **kwargs):
    '''
    Get the credits (cast and crew) that have been added to a TV show.

    required: tv_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/credits', disable_cache, params=kwargs)

def episode_groups(tv_id, disable_cache=False, **kwargs):
    '''
    Get all of the episode groups that have been created for a TV show.
    With a group ID you can call the https://developers.themoviedb.org/3/tv-episode-groups/get-tv-episode-group-details method.

    required: tv_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/episode_groups', disable_cache, params=kwargs)

def external_ids(tv_id, disable_cache=False, **kwargs):
    '''
    Get the external ids for a TV show. We currently support the following external sources.

    Media Databases
        IMDb ID
        TVDB ID
        Freebase MID*
        Freebase ID*
        TVRage ID*
    Social IDs
        Facebook
        Instagram
        Twitter

    *Defunct or no longer available as a service.

    required: tv_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/external_ids', disable_cache, params=kwargs)

def images(tv_id, disable_cache=False, **kwargs):
    '''
    Get the images that belong to a TV show.
    Querying images with a language parameter will filter the results.
    If you want to include a fallback language (especially useful for backdrops) you can use the include_image_language parameter.
    This should be a comma seperated value like so: include_image_language=en,null.

    required: tv_id
    optional: language, include_image_language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/images', disable_cache, params=kwargs)

def keywords(tv_id, disable_cache=False):
    '''
    Get the keywords that have been added to a TV show.

    required: tv_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/keywords', disable_cache)

def recommendations(tv_id, disable_cache=False, **kwargs):
    '''
    Get the list of TV show recommendations for this item.

    required: tv_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/recommendations', disable_cache, params=kwargs)

def reviews(tv_id, disable_cache=False, **kwargs):
    '''
    Get the reviews for a TV show.

    required: tv_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/reviews', disable_cache, params=kwargs)

def screened_theatrically(tv_id, disable_cache=False):
    '''
    Get a list of seasons or episodes that have been screened in a film festival or theatre.

    required: tv_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/screened_theatrically', disable_cache)

def similar(tv_id, disable_cache=False, **kwargs):
    '''
    Get a list of similar TV shows.
    These items are assembled by looking at keywords and genres.

    required: tv_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/similar', disable_cache, params=kwargs)

def translations(tv_id, disable_cache=False, **kwargs):
    '''
    Get a list of the translations that exist for a TV show.

    required: tv_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/translations', disable_cache, params=kwargs)

def videos(tv_id, disable_cache=False, **kwargs):
    '''
    Get the videos that have been added to a TV show.

    required: tv_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/{tv_id}/videos', disable_cache, params=kwargs)

def latest(disable_cache=False, **kwargs):
    '''
    Get the most newly created TV show. This is a live response and will continuously change.

    required: 
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/latest', disable_cache, params=kwargs)

def airing_today(disable_cache=False, **kwargs):
    '''
    Get a list of TV shows that are airing today. This query is purely day based as we do not currently support airing times.
    You can specify a timezone to offset the day calculation. Without a specified timezone, this query defaults to EST (Eastern Time UTC-05:00).

    required: 
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/airing_today', disable_cache, params=kwargs)

def on_the_air(disable_cache=False, **kwargs):
    '''
    Get a list of shows that are currently on the air.
    This query looks for any TV show that has an episode with an air date in the next 7 days.

    required: 
    optional: page, language, region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/on_the_air', disable_cache, params=kwargs)

def popular(disable_cache=False, **kwargs):
    '''
    Get a list of the current popular TV shows on TMDb. This list updates daily.

    required: 
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/popular', disable_cache, params=kwargs)

def top_rated(disable_cache=False, **kwargs):
    '''
    Get a list of the top rated TV shows on TMDb.

    required: 
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/top_rated', disable_cache, params=kwargs)

def rate_movie(tv_id, rating, **kwargs):
    '''
    Rate a TV show.
    A valid session or guest session ID is required. You can read more about how this works: https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id

    required: tv_id, rating, session_id or guest_session_id
    optional: 
    '''

    payload = "{\"value\": \""+str(rating)+"\"}"

    return _call('POST', f'https://api.themoviedb.org/3/tv/{tv_id}/rating', True, params=kwargs, payload=payload)

def delete_rating(tv_id, **kwargs):
    '''
    Remove your rating for a TV show.
    A valid session or guest session ID is required. You can read more about how this works: https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id

    required: tv_id, session_id or guest_session_id
    optional: 
    '''

    return _call('DELETE', f'https://api.themoviedb.org/3/tv/{tv_id}/rating', True, params=kwargs)