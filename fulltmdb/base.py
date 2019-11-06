from time import time, sleep
from os import environ
from requests import request
import requests_cache

requests_cache.install_cache(cache_name='TMDB-cache', backend='sqlite', expire_after=3600)
environ["remaining"] = "40"

class Setup():
    def purge_cache():
        requests_cache.remove_expired_responses()

    def set_api_key(api_key):
        environ["TMDB_API_KEY"] = api_key

    def set_read_access_token(access_token):
        environ["TMDB_READ_ACCESS_TOKEN"] = access_token

def _get_api_key():
    return f'api_key={environ.get("TMDB_API_KEY")}'

def _get_read_access_token():
    return environ.get("TMDB_READ_ACCESS_TOKEN")

def _get_url():
    return "https://api.themoviedb.org/"

def _get_obj(result):
    if "success" in result and result["success"] is False:
        raise Exception(result["status_message"])
    
    return _AsObj(**result)

def _call(request_type, url, headers=None, params=None, payload=None, disable_cache=None):
    if disable_cache:
        with requests_cache.disabled():
            req = request(request_type, url, params=params, data=payload, headers=headers)
    else:
        req = request(request_type, url, params=params, data=payload, headers=headers)
    headers = req.headers
    if "X-RateLimit-Remaining" in headers:
        environ["remaining"] = headers["X-RateLimit-Remaining"]

    if "X-RateLimit-Reset" in headers:
        environ["reset"] = headers["X-RateLimit-Reset"]

    if int(environ.get("remaining")) < 1:
        current_time = int(time())
        sleep_time = int(environ.get("reset")) - current_time
        print("Rate limit reached. Sleeping for: %d" % sleep_time)
        sleep(abs(sleep_time))
        _call(request_type, url, headers, payload)

    json = req.json()

    return _get_obj(json)

class _AsObj:
    def __init__(self, **entries):
        self.__dict__.update(entries)
