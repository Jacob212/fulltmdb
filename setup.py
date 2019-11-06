import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fulltmdb",
    version = "0.0.1",
    author = "Jacob Hale",
    author_email = "jacobhale.hale@gmail.com",
    description = ("A wrapper for The Movie Database API v3 and v4."),
    keywords = ['movie', 'the movie database', 'movie database', 'tmdb', 
                'wrapper', 'database', 'themoviedb', 'moviedb', 'api'],
    url = "https://github.com/Jacob212/fulltmdb",
    packages=['requests', 'requests_cache','time'],
    long_description=read('README'),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
)