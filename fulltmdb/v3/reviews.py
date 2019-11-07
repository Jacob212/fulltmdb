from ..base import _call, _get_read_access_token

'''
All api requests under the reviews tab in https://developers.themoviedb.org/3/reviews
'''

def details(review_id):
    '''

    required: review_id
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/review/{review_id}', headers=headers)
