from ..base import _call, _get_read_access_token

'''
All api requests under the people tab in https://developers.themoviedb.org/3/people
'''

def details(person_id, **kwargs):
    '''
    Get the primary person details by id.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: person_id
    optional: language, append_to_response
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}', params=kwargs, headers=headers)

def changes(person_id, **kwargs):
    '''
    Get the changes for a person. By default only the last 24 hours are returned.
    You can query up to 14 days in a single query by using the start_date and end_date query parameters.

    required: person_id
    optional: page, start_date, end_date
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}/changes', params=kwargs, headers=headers)

def movie_credits(person_id, **kwargs):
    '''
    Get the movie credits for a person.

    required: person_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}/movie_credits', params=kwargs, headers=headers)

def combined_credits(person_id, **kwargs):
    '''
    Get the movie and TV credits together in a single response.

    required: person_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}/combined_credits', params=kwargs, headers=headers)

def external_ids(person_id, **kwargs):
    '''
    Get the external ids for a person. We currently support the following external sources.
    External Sources
    IMDB ID
    Facebook
    Freebase MID
    Freebase ID
    Instagram
    TVRage ID
    Twitter

    required: person_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}/external_ids', params=kwargs, headers=headers)

def images(person_id):
    '''
    Get the images for a person.

    required: person_id
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}/images', headers=headers)

def details(person_id, **kwargs):
    '''
    Get the primary person details by id.
    Supports append_to_response. https://developers.themoviedb.org/3/getting-started/append-to-response

    required: person_id
    optional: language, append_to_response
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}', params=kwargs, headers=headers)

def tagged_images(person_id, **kwargs):
    '''
    Get the images that this person has been tagged in.

    required: person_id
    optional: language, page
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}/tagged_images', params=kwargs, headers=headers)

def translations(person_id, **kwargs):
    '''
    Get a list of translations that have been created for a person.

    required: person_id
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/{person_id}/translations', params=kwargs, headers=headers)

def latest(**kwargs):
    '''
    Get the most newly created person. This is a live response and will continuously change.

    required:
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/latest', params=kwargs, headers=headers)

def popular(**kwargs):
    '''
    Get the list of popular people on TMDb. This list updates daily.

    required:
    optional: language
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/popular', params=kwargs, headers=headers)
