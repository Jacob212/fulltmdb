from ..base import _call

'''
All api requests under the find tab in https://developers.themoviedb.org/3/find
'''

def id(external_id, disable_cache=False, **kwargs):
    '''
    The find method makes it easy to search for objects in our database by an external id. For example, an IMDB ID.
    This method will search all objects (movies, TV shows and people) and return the results in a single response.
    The supported external sources for each object are as follows.

    Media Databases
                   Movies       TV Shows        TV Seasons      TV Episodes         People
    IMDb ID        ✓            ✓               ✗               ✓                  ✓
    TVDB ID        ✗            ✓               ✓               ✓                  ✗
    Freebase MID*  ✗            ✓               ✓               ✓                  ✓
    Freebase ID*   ✗            ✓               ✓               ✓                  ✓
    TVRage ID*     ✗            ✓               ✓               ✓                  ✓


    Social IDs
                Movies      TV Shows        TV Seasons      TV Episodes         People
    Facebook     ✓          ✓               ✗               ✗                   ✓
    Instagram    ✓          ✓               ✗               ✗                   ✓
    Twitter      ✓          ✓               ✗               ✗                   ✓

    *Defunct or no longer available as a service.

    required: external_id, external_source
    optional: language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/find/{external_id}', disable_cache, params=kwargs)
