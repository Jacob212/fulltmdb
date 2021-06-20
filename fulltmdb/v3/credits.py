from ..base import _call

'''
All api requests under the credits tab in https://developers.themoviedb.org/3/credits
'''

def details(credit_id, disable_cache=False):
    '''
    Get a movie or TV credit details by id.

    required: credit_id
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/credit/{credit_id}', disable_cache)
