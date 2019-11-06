from ..base import _call, _get_read_access_token

'''
All api requests under the discover tab in https://developers.themoviedb.org/3/discover
'''

def movie(**kwargs):
    '''
    Discover movies by different types of data like average rating, number of votes, genres and certifications.
    You can get a valid list of certifications from the https://developers.themoviedb.org/3/certifications/get-movie-certifications method.

    Discover also supports a nice list of sort options. See below for all of the available options.

    Please note, when using certification/certification.lte you must also specify certification_country.
    These two parameters work together in order to filter the results.
    You can only filter results with the countries we have added to our https://developers.themoviedb.org/3/certifications/get-movie-certifications.

    If you specify the region parameter, the regional release date will be used instead of the primary release date.
    The date returned will be the first date based on your query (ie. if a with_release_type is specified).
    It's important to note the order of the release types that are used.
    Specifying "2|3" would return the limited theatrical release date as opposed to "3|2" which would return the theatrical date.

    Also note that a number of filters support being comma (,) or pipe (|) separated. Comma's are treated like an AND and query while pipe's are an OR.

    Some examples of what can be done with discover can be found https://www.themoviedb.org/documentation/api/discover.

    required: 
    optional: language, region, sort_by, certification_country, certification, certification.lte, certification.gte, include_adult, include_video, page, 
            primary_release_year, primary_release_date.gte, primary_release_date.lte, release_date.gte, release_date.lte,
            with_release_type, year, vote_count.gte, vote_count.lte, vote_average.gte, vote_average.lte, with_cast, with_crew,
            with_people, with_companies, with_genres, without_genres, with_keywords, without_keywords, with_runtime.gte, with_runtime.lte, with_original_language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/discover/movie', params=kwargs, headers=headers)

def tv(**kwargs):
    '''
    Discover TV shows by different types of data like average rating, number of votes, genres, the network they aired on and air dates.

    Discover also supports a nice list of sort options. See below for all of the available options.

    Also note that a number of filters support being comma (,) or pipe (|) separated. Comma's are treated like an AND and query while pipe's are an OR.

    Some examples of what can be done with discover can be found https://www.themoviedb.org/documentation/api/discover.

    required: 
    optional: language, sort_by, air_date.gte, air_date.lte, first_air_date.gte, first_air_date.lte, first_air_date_year,
            page, timezone, vote_count.gte, vote_count.lte, vote_average.gte, vote_average.lte, with_networks, with_companies, with_genres,
            without_genres, with_keywords, without_keywords, with_runtime.gte, with_runtime.lte, with_original_language, screened_theatrically, include_null_first_air_dates
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/discover/tv', params=kwargs, headers=headers)
