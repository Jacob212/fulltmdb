from ..base import _call, _get_read_access_token

'''
All api requests under the auth tab in https://developers.themoviedb.org/4/auth

https://developers.themoviedb.org/4/auth/user-authorization-1
'''

def create_request_token(redirect_to=''):
    '''
    This method generates a new request token that you can ask a user to approve.
    This is the first step in getting permission from a user to read and write data on their behalf.

    Note that there is an optional body you can post alongside this request to set a redirect URL or callback that will be executed once a request token has been approved on TMDb.

    required:
    optional: redirect_to
    '''

    payload = {
        'redirect_to': redirect_to
    }

    headers = {
        'authorization': f'Bearer {_get_read_access_token()}',
        'content-type': 'application/json;charset=utf-8'
        }

    return _call('POST', f'https://api.themoviedb.org/4/auth/request_token', headers=headers, payload=payload)

def create_access_token(request_token):
    '''
    This method will finish the user authentication flow and issue an official user access token.
    The request token in this request is sent along as part of the POST body.
    You should still use your standard API read access token for authenticating this request.

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

    return _call('GET', f'https://api.themoviedb.org/4/auth/access_token', headers=headers, payload=payload)

def delete_access_token(access_token):
    '''
    This method gives your users the ability to log out of a session.

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

    return _call('POST', f'https://api.themoviedb.org/4/auth/access_token', headers=headers, payload=payload)
