from ..base import _call

'''
All api requests under the cerifications tab in https://developers.themoviedb.org/3/cerifications
'''

def movie():
    '''
    Get an up to date list of the officially supported movie certifications on TMDb.

    required: 
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/certification/movie/list')

def tv():
    '''
    Get an up to date list of the officially supported TV show certifications on TMDb.

    required: 
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/certification/tv/list')
