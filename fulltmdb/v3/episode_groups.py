from ..base import _call

'''
All api requests under the tv episode groups tab in https://developers.themoviedb.org/3/tv-episode-groups
'''

def details(group_id, **kwargs):
    '''
    Get the details of a TV episode group. Groups support 7 different types which are enumerated as the following:

        Original air date
        Absolute
        DVD
        Digital
        Story arc
        Production
        TV

    required: group_id
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/tv/episode_group/{group_id}', params=kwargs)
