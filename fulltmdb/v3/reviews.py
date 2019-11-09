from ..base import _call

'''
All api requests under the reviews tab in https://developers.themoviedb.org/3/reviews
'''

def details(review_id):
    '''

    required: review_id
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/review/{review_id}')
