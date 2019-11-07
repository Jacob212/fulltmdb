import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(
    name='fulltmdb',
    version='0.0.2',
    author='Jacob Hale',
    author_email='jacobhale.hale@gmail.com',
    description=('A wrapper for The Movie Database API v3 and v4.'),
    keywords=['tmdb', 'api-wrapper'],
    url='https://github.com/Jacob212/fulltmdb',
    packages=['fulltmdb','fulltmdb.v3','fulltmdb.v4'],
    test_suite='test',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=['requests', 'requests_cache'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
)
