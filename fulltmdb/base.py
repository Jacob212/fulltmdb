from time import time, sleep
from os import environ
from requests import request
import requests_cache

environ['remaining'] = '40'

class Setup():
    def set_read_access_token(access_token):
        environ['TMDB_READ_ACCESS_TOKEN'] = access_token

    def set_cache(expire_after):
        requests_cache.install_cache(cache_name='TMDB-cache', backend='sqlite', expire_after=expire_after)

    def purge_cache():
        requests_cache.remove_expired_responses()

def _get_read_access_token():
    return environ.get('TMDB_READ_ACCESS_TOKEN')

def _check_status(result):
    if 'success' in result and result['success'] is False:
        raise Exception(result['status_message'])
    return result

def _call(request_type, url, headers=None, params=None, payload=None, disable_cache=None):
    if disable_cache:
        with requests_cache.disabled():
            req = request(request_type, url, params=params, data=payload, headers=headers)
    else:
        req = request(request_type, url, params=params, data=payload, headers=headers)
    headers = req.headers
    if 'X-RateLimit-Remaining' in headers:
        environ['remaining'] = headers['X-RateLimit-Remaining']

    if 'X-RateLimit-Reset' in headers:
        environ['reset'] = headers['X-RateLimit-Reset']

    if int(environ.get('remaining')) < 1:
        current_time = int(time())
        sleep_time = int(environ.get('reset')) - current_time
        print('Rate limit reached. Sleeping for: %d' % sleep_time)
        sleep(abs(sleep_time))
        _call(request_type, url, headers, payload)

    json = req.json()

    return _check_status(json)
