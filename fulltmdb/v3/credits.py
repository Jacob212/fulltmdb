from ..base import _call, _get_read_access_token

'''
All api requests under the credits tab in https://developers.themoviedb.org/3/credits
'''

def details(credit_id):
    '''
    Get a movie or TV credit details by id.

    required: credit_id
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/credit/{credit_id}', headers=headers)
