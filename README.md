# fulltmdb
A wrapper for The Movie Database API v3 and v4 that only uses the read access token (not api key).

![](https://github.com/Jacob212/fulltmdb/workflows/Build/badge.svg)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fulltmdb.

```bash
pip install fulltmdb
```

## Read Access Token

To use this package you will need a read access token from The Movie Database. To get one, follow these steps:

1) Create an account on [TMDB](https://www.themoviedb.org/account/signup)
2) Then you can request an api key form [here](https://www.themoviedb.org/settings/api/request)
3) Once your request as been aproved you can go to [here](https://www.themoviedb.org/settings/api) and copy the read access token at the bottom.

## Basic Usage

```python
from fulltmdb import setup, movies

setup.set_read_access_token('YOUR_READ_ACCESS_TOKEN')
setup.set_cache(3600)#Set the cache expire time. If you don't want to cache then remove this line.

result = movies.popular()
#returns a dictionary object with page, results, total_results and total_pages as keys.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.