from ..base import _call, _get_read_access_token

'''
All api requests under the configuration tab in https://developers.themoviedb.org/3/configuration
'''

def api():
    '''
    Get the system wide configuration information. Some elements of the API require some knowledge of this configuration data.
    The purpose of this is to try and keep the actual API responses as light as possible.
    It is recommended you cache this data within your application and check for updates every few days.

    This method currently holds the data relevant to building image URLs as well as the change key map.

    To build an image URL, you will need 3 pieces of data. The base_url, size and file_path.
    Simply combine them all and you will have a fully qualified URL. Here’s an example URL:
    https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg
    The configuration method also contains the list of change keys which can be useful if you are building an app that consumes data from the change feed.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/configuration', headers=headers)

def countries():
    '''
    Get the list of countries (ISO 3166-1 tags) used throughout TMDb.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/configuration/countries', headers=headers)

def jobs():
    '''
    Get a list of the jobs and departments we use on TMDb.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/configuration/jobs', headers=headers)

def languages():
    '''
    Get the list of languages (ISO 639-1 tags) used throughout TMDb.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/configuration/languages', headers=headers)

def primary_translations():
    '''
    Get a list of the officially supported translations on TMDb.

    While it's technically possible to add a translation in any one of the https://developers.themoviedb.org/3/configuration/get-languages we have added to TMDb (we don't restrict content),
    the ones listed in this method are the ones we also support for localizing the website with which means they are what we refer to as the "primary" translations.

    These are all specified as https://en.wikipedia.org/wiki/IETF_language_tag to identify the languages we use on TMDb. There is one exception which is image languages.
    They are currently only designated by a ISO-639-1 tag. This is a planned upgrade for the future.

    We're always open to adding more if you think one should be added. You can ask about getting a new primary translation added by posting on https://www.themoviedb.org/talk/category/5047951f760ee3318900009a.

    One more thing to mention, these are the translations that map to our website translation project. You can view and contribute to that project https://app.localeapp.com/projects/8267.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/configuration/primary_translations', headers=headers)

def timezones():
    '''
    Get the list of timezones used throughout TMDb.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/configuration/timezones', headers=headers)
