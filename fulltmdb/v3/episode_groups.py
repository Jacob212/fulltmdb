from ..base import _call, _get_read_access_token

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

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/tv/episode_group/{group_id}', params=kwargs, headers=headers)
