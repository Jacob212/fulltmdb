from ..base import _call, _get_read_access_token

'''
All api requests under the cerifications tab in https://developers.themoviedb.org/3/cerifications
'''

def movie():
    '''
    Get an up to date list of the officially supported movie certifications on TMDb.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/certification/movie/list', headers=headers)

def tv():
    '''
    Get an up to date list of the officially supported TV show certifications on TMDb.

    required: 
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/certification/tv/list', headers=headers)
