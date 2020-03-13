from ..base import _call

'''
All api requests under the account tab in https://developers.themoviedb.org/3/account
'''

def details(session_id):
    '''
    Get your account details.

    required: session_id 
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account?session_id={session_id}')

def created_lists(account_id, **kwargs):
    '''
    Get all of the lists created by an account. Will include private lists if you are the owner.

    required: session_id, account_id
    optional: page, language
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/lists', params=kwargs)

def favorite_movies(account_id, **kwargs):
    '''
    Get the list of your favorite movies.

    required: session_id, account_id
    optional: page, language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/favorite/movies', params=kwargs)

def favorite_tv_shows(account_id, **kwargs):
    '''
    Get the list of your favorite TV shows.

    required: session_id, account_id
    optional: page, language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/favorite/tv', params=kwargs)

def mark_as_favorite(account_id, session_id, media_type, media_id, favorite):
    '''
    This method allows you to mark a movie or TV show as a favorite item.

    required: session_id, account_id, media_type, media_id
    optional:
    '''

    payload = "{\"media_type\": \""+media_type+"\", \"media_id\": \""+str(media_id)+"\", \"favorite\": \""+str(favorite)+"\"}"

    return _call('POST', f'https://api.themoviedb.org/3/account/{account_id}/favorite?session_id={session_id}', payload=payload)

def rated_movies(account_id, **kwargs):
    '''
    Get a list of all the movies you have rated.

    required: session_id, account_id
    optional: page, language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/rated/movies', params=kwargs)

def rated_tv(account_id, **kwargs):
    '''
    Get a list of all the TV shows you have rated.

    required: session_id, account_id
    optional: page, language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/rated/tv', params=kwargs)

def rated_tv_episodes(account_id, **kwargs):
    '''
    Get a list of all the TV episodes you have rated.

    required: session_id, account_id
    optional: page, language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/rated/tv/episodes', params=kwargs)

def movie_watchlist(account_id, **kwargs):
    '''
    Get a list of all the movies you have added to your watchlist.

    required: session_id, account_id
    optional: page, language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/watchlist/movies', params=kwargs)

def tv_show_watchlist(account_id, **kwargs):
    '''
    Get a list of all the TV shows you have added to your watchlist.

    required: session_id, account_id
    optional: page, language, sort_by
    '''

    return _call('GET', f'https://api.themoviedb.org/3/account/{account_id}/watchlist/tv', params=kwargs)

def add_to_watchlist(account_id, session_id, media_type, media_id, watchlist):
    '''
    Add a movie or TV show to your watchlist.

    required: session_id, account_id, media_type, media_id
    optional:
    '''

    payload = "{\"media_type\": \""+media_type+"\", \"media_id\": \""+str(media_id)+"\", \"watchlist\": \""+str(watchlist)+"\"}"

    return _call('POST', f'https://api.themoviedb.org/3/account/{account_id}/watchlist?session_id={session_id}', payload=payload)