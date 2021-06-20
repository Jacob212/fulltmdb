from ..base import _call

'''
All api requests under the movies tab in https://developers.themoviedb.org/3/movies
'''


def details(movie_id, disable_cache=False, **kwargs):
    '''
    Get the primary information about a movie.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: movie_id
    optional: language, append_to_response
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}', disable_cache, params=kwargs)


def account_states(movie_id, disable_cache=False, **kwargs):
    '''
    Grab the following account states for a session:
        Movie rating
        If it belongs to your watchlist
        If it belongs to your favourite list

    required: movie_id, session_id or guest_session_id
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/account_states', disable_cache, params=kwargs)


def alternative_titles(movie_id, disable_cache=False, **kwargs):
    '''
    Get all of the alternative titles for a movie.

    required: movie_id
    optional: country
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/alternative_titles', disable_cache, params=kwargs)


def changes(movie_id, disable_cache=False, **kwargs):
    '''
    Get the changes for a movie. By default only the last 24 hours are returned.
    You can query up to 14 days in a single query by using the start_date and end_date query parameters.

    required: movie_id
    optional: page, start_date, end_date
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/changes', disable_cache, params=kwargs)


def credits(movie_id, disable_cache=False):
    '''
    Get the cast and crew for a movie.

    required: movie_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/credits', disable_cache)


def external_ids(movie_id, disable_cache=False):
    '''
    Get the external ids for a movie. We currently support the following external sources.

    Media Databases: 
        IMDb ID 
    Social IDs:
        Facebook
        Instagram
        Twitter

    required: movie_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/external_ids', disable_cache)


def images(movie_id, disable_cache=False, **kwargs):
    '''
    Get the images that belong to a movie.
    Querying images with a language parameter will filter the results.
    If you want to include a fallback language (especially useful for backdrops) you can use the include_image_language parameter.
    This should be a comma seperated value like so: include_image_language=en,null.

    required: movie_id
    optional: language, include_image_language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/images', disable_cache, params=kwargs)


def keywords(movie_id, disable_cache=False):
    '''
    Get the keywords that have been added to a movie.

    required: movie_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/keywords', disable_cache)


def release_dates(movie_id, disable_cache=False):
    '''
    Get the release date along with the certification for a movie.
    Release dates support different types:
        Premiere
        Theatrical (limited)
        Theatrical
        Digital
        Physical
        TV

    required: movie_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/release_dates', disable_cache)


def videos(movie_id, disable_cache=False, **kwargs):
    '''
    Get the videos that have been added to a movie.

    required: movie_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/videos', disable_cache, params=kwargs)


def translations(movie_id, disable_cache=False):
    '''
    Get a list of translations that have been created for a movie.

    required: movie_id
    optional: 
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/translations', disable_cache)


def recommendations(movie_id, disable_cache=False, **kwargs):
    '''
    Get a list of recommended movies for a movie.

    required: movie_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations', disable_cache, params=kwargs)


def similar(movie_id, disable_cache=False, **kwargs):
    '''
    Get a list of similar movies. This is not the same as the 'Recommendation' system you see on the website.
    These items are assembled by looking at keywords and genres.

    required: movie_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/similar', disable_cache, params=kwargs)


def reviews(movie_id, disable_cache=False, **kwargs):
    '''
    Get the user reviews for a movie.

    required: movie_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/reviews', disable_cache, params=kwargs)


def lists(movie_id, disable_cache=False, **kwargs):
    '''
    Get a list of lists that this movie belongs to.

    required: movie_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/lists', disable_cache, params=kwargs)


def latest(disable_cache=False, **kwargs):
    '''
    Get the most newly created movie. This is a live response and will continuously change.

    required: 
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/latest', disable_cache, params=kwargs)


def now_playing(disable_cache=False, **kwargs):
    '''
    Get a list of movies in theatres. This is a release type query that looks for all movies that have a release type of 2 or 3 within the specified date range.
    You can optionally specify a region prameter which will narrow the search to only look for theatrical release dates within the specified country.

    required: 
    optional: page, language, region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/now_playing', disable_cache, params=kwargs)


def popular(disable_cache=False, **kwargs):
    '''
    Get a list of the current popular movies on TMDb. This list updates daily.

    required: 
    optional: page, language, region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/popular', disable_cache, params=kwargs)


def top_rated(disable_cache=False, **kwargs):
    '''
    Get the top rated movies on TMDb.

    required: 
    optional: page, language, region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/top_rated', disable_cache, params=kwargs)


def upcoming(disable_cache=False, **kwargs):
    '''
    Get a list of upcoming movies in theatres. This is a release type query that looks for all movies that have a release type of 2 or 3 within the specified date range.
    You can optionally specify a region prameter which will narrow the search to only look for theatrical release dates within the specified country.

    required: 
    optional: page, language, region
    '''

    return _call('GET', f'https://api.themoviedb.org/3/movie/upcoming', disable_cache, params=kwargs)


def rate_movie(movie_id, rating, **kwargs):
    '''
    Rate a movie.
    A valid session or guest session ID is required. You can read more about how this works: https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id

    required: movie_id, rating, session_id or guest_session_id
    optional: 
    '''

    payload = "{\"value\": \""+str(rating)+"\"}"

    return _call('POST', f'https://api.themoviedb.org/3/movie/{movie_id}/rating', True, params=kwargs, payload=payload)


def delete_rating(movie_id, **kwargs):
    '''
    Remove your rating for a movie.
    A valid session or guest session ID is required. You can read more about how this works: https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id

    required: movie_id, session_id or guest_session_id
    optional: 
    '''

    return _call('DELETE', f'https://api.themoviedb.org/3/movie/{movie_id}/rating', True, params=kwargs)
