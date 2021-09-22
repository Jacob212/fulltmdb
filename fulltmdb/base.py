from os import environ
from requests import request
import requests_cache

use_json = True

class Setup():
    def set_read_access_token(access_token):
        environ['TMDB_READ_ACCESS_TOKEN'] = access_token

    def set_cache(expire_after):
        requests_cache.install_cache(cache_name='TMDB-cache', backend='sqlite', expire_after=expire_after)

    def purge_cache():
        requests_cache.remove_expired_responses()

    def clear_cache():
        requests_cache.clear()
    
    def just_json(option):
        global use_json
        use_json = option

def _get_read_access_token():
    return environ.get('TMDB_READ_ACCESS_TOKEN')

def _check_status(result):
    if 'success' in result and result['success'] is False:
        raise Exception(result['status_message'])
    return result

def _call(request_type, url, disable_cache, bearer=None, params=None, payload=None):
    if bearer is None:
        headers = {
            'authorization': f'Bearer {_get_read_access_token()}',
            'content-type': 'application/json;charset=utf-8'
        }
    else:
        headers = {
            'authorization': f'Bearer {bearer}',
            'content-type': 'application/json;charset=utf-8'
        }
    if disable_cache:
        with requests_cache.disabled():
            req = request(request_type, url, params=params, data=payload, headers=headers)
    else:
        req = request(request_type, url, params=params, data=payload, headers=headers)

    json = req.json()

    if use_json:
        return _check_status(json)
    return req