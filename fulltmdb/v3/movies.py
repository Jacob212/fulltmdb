from ..base import _call, _get_read_access_token

'''
All api requests under the movies tab in https://developers.themoviedb.org/3/movies
'''

def details(movie_id, **kwargs):
    '''
    Get the primary information about a movie.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: movie_id
    optional: language, append_to_response
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}', params=kwargs, headers=headers)

def account_states(movie_id, **kwargs):
    '''
    Grab the following account states for a session:
        Movie rating
        If it belongs to your watchlist
        If it belongs to your favourite list

    required: movie_id, session_id or guest_session_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/account_states', params=kwargs, headers=headers)

def alternative_titles(movie_id, **kwargs):
    '''
    Get all of the alternative titles for a movie.

    required: movie_id
    optional: country
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/alternative_titles', params=kwargs, headers=headers)

def changes(movie_id, **kwargs):
    '''
    Get the changes for a movie. By default only the last 24 hours are returned.
    You can query up to 14 days in a single query by using the start_date and end_date query parameters.

    required: movie_id
    optional: page, start_date, end_date
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/changes', params=kwargs, headers=headers)

def credits(movie_id):
    '''
    Get the cast and crew for a movie.

    required: movie_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/credits', headers=headers)

def external_ids(movie_id):
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

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/external_ids', headers=headers)

def images(movie_id, **kwargs):
    '''
    Get the images that belong to a movie.
    Querying images with a language parameter will filter the results.
    If you want to include a fallback language (especially useful for backdrops) you can use the include_image_language parameter.
    This should be a comma seperated value like so: include_image_language=en,null.

    required: movie_id
    optional: language, include_image_language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/images', params=kwargs, headers=headers)

def keywords(movie_id):
    '''
    Get the keywords that have been added to a movie.

    required: movie_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/keywords', headers=headers)

def release_dates(movie_id):
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

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/release_dates', headers=headers)

def videos(movie_id, **kwargs):
    '''
    Get the videos that have been added to a movie.

    required: movie_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/videos', params=kwargs, headers=headers)

def translations(movie_id):
    '''
    Get a list of translations that have been created for a movie.

    required: movie_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/translations', headers=headers)

def recommendations(movie_id, **kwargs):
    '''
    Get a list of recommended movies for a movie.

    required: movie_id
    optional: page, language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations', params=kwargs, headers=headers)

def similar(movie_id, **kwargs):
    '''
    Get a list of similar movies. This is not the same as the 'Recommendation' system you see on the website.
    These items are assembled by looking at keywords and genres.

    required: movie_id
    optional: page, language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/similar', params=kwargs, headers=headers)

def reviews(movie_id, **kwargs):
    '''
    Get the user reviews for a movie.

    required: movie_id
    optional: page, language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/reviews', params=kwargs, headers=headers)

def lists(movie_id, **kwargs):
    '''
    Get a list of lists that this movie belongs to.

    required: movie_id
    optional: page, language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/{movie_id}/lists', params=kwargs, headers=headers)

def latest(**kwargs):
    '''
    Get the most newly created movie. This is a live response and will continuously change.

    required: 
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/latest', params=kwargs, headers=headers)

def now_playing(**kwargs):
    '''
    Get a list of movies in theatres. This is a release type query that looks for all movies that have a release type of 2 or 3 within the specified date range.
    You can optionally specify a region prameter which will narrow the search to only look for theatrical release dates within the specified country.

    required: 
    optional: page, language, region
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/now_playing', params=kwargs, headers=headers)

def popular(**kwargs):
    '''
    Get a list of the current popular movies on TMDb. This list updates daily.

    required: 
    optional: page, language, region
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/popular', params=kwargs, headers=headers)

def top_rated(**kwargs):
    '''
    Get the top rated movies on TMDb.

    required: 
    optional: page, language, region
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/top_rated', params=kwargs, headers=headers)

def upcoming(**kwargs):
    '''
    Get a list of upcoming movies in theatres. This is a release type query that looks for all movies that have a release type of 2 or 3 within the specified date range.
    You can optionally specify a region prameter which will narrow the search to only look for theatrical release dates within the specified country.

    required: 
    optional: page, language, region
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/upcoming', params=kwargs, headers=headers)

def rate_movie(movie_id, rating, **kwargs):
    '''
    Rate a movie.
    A valid session or guest session ID is required. You can read more about how this works: https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id

    required: movie_id, rating, session_id or guest_session_id
    optional: 
    '''

    payload = {
        'value': rating
        }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/movie/{movie_id}/rating', params=kwargs, headers=headers, payload=payload)

def delete_rating(movie_id, **kwargs):
    '''
    Remove your rating for a movie.
    A valid session or guest session ID is required. You can read more about how this works: https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id

    required: movie_id, session_id or guest_session_id
    optional: 
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('DELETE', f'https://api.themoviedb.org/3/movie/{movie_id}/rating', params=kwargs, headers=headers)