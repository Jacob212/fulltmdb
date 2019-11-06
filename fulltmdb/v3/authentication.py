from ..base import _call, _get_read_access_token

'''
All api requests under the authentication tab in https://developers.themoviedb.org/3/authentication

https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id
'''

def create_guest_session():
    '''
    This method will let you create a new guest session.
    Guest sessions are a type of session that will let a user rate movies and TV shows but not require them to have a TMDb user account.
    More information about user authentication can be found https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

    Please note, you should only generate a single guest session per user (or device) as you will be able to attach the ratings to a TMDb user account in the future.
    There is also IP limits in place so you should always make sure it's the end user doing the guest session actions.

    If a guest session is not used for the first time within 24 hours, it will be automatically deleted.

    required:
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/authentication/guest_session/new', headers=headers)

def create_request_token():
    '''
    Create a temporary request token that can be used to validate a TMDb user login. More details about how this works can be found https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

    required:
    optional:
    '''

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('GET', f'https://api.themoviedb.org/3/authentication/token/new', headers=headers)

def create_request_token(request_token):
    '''
    You can use this method to create a fully valid session ID once a user has validated the request token.
    More information about how this works can be found https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

    required: request_token
    optional:
    '''

    payload = {
        'request_token': request_token
    }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/authentication/session/new', headers=headers, payload=payload)

def create_request_token(username, password, request_token):
    '''
    This method allows an application to validate a request token by entering a username and password.

    Not all applications have access to a web view so this can be used as a substitute.

    Please note, the preferred method of validating a request token is to have a user authenticate the request via the TMDb website.
    You can read about that method https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

    If you decide to use this method please use HTTPS.

    required: username, password, request_token
    optional:
    '''

    payload = {
        'username': username,
        'password': password,
        'request_token': request_token
    }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/authentication/token/validate_with_login', headers=headers, payload=payload)

def create_request_token(access_token):
    '''
    Use this method to create a v3 session ID if you already have a valid v4 access token.
    The v4 token needs to be authenticated by the user.
    Your standard "read token" will not validate to create a session ID.

    required: access_token
    optional:
    '''

    payload = {
        'access_token': access_token
    }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/3/authentication/session/convert/4', headers=headers, payload=payload)

def create_request_token(session_id):
    '''
    If you would like to delete (or "logout") from a session, call this method with a valid session ID.

    required: session_id
    optional:
    '''

    payload = {
        'session_id': session_id
    }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('DELETE', f'https://api.themoviedb.org/3/authentication/session', headers=headers, payload=payload)
