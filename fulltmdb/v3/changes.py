from ..base import _call, _get_read_access_token

'''
All api requests under the changes tab in https://developers.themoviedb.org/3/changes
'''

def movie(**kwargs):
    '''
    Get a list of all of the movie ids that have been changed in the past 24 hours.
    You can query it for up to 14 days worth of changed IDs at a time with the start_date and end_date query parameters.
    100 items are returned per page.

    required: 
    optional: page, start_date, end_date
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/movie/changes', params=kwargs, headers=headers)

def tv(**kwargs):
    '''
    Get a list of all of the TV show ids that have been changed in the past 24 hours.
    You can query it for up to 14 days worth of changed IDs at a time with the start_date and end_date query parameters.
    100 items are returned per page.

    required: 
    optional: page, start_date, end_date
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/changes', params=kwargs, headers=headers)

def person(**kwargs):
    '''
    Get a list of all of the person ids that have been changed in the past 24 hours.
    You can query it for up to 14 days worth of changed IDs at a time with the start_date and end_date query parameters.
    100 items are returned per page.

    required: 
    optional: page, start_date, end_date
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/person/changes', params=kwargs, headers=headers)