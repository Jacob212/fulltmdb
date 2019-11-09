from ..base import _call

'''
All api requests under the trending tab in https://developers.themoviedb.org/3/trending
'''

def trending(media_type, time_window):
    '''
    Get the daily or weekly trending items.
    The daily trending list tracks items over the period of a day while items have a 24 hour half life.
    The weekly list tracks items over a 7 day period, with a 7 day half life.

    Valid Media Types
    Media Type      Description
    all             Include all movies, TV shows and people in the results as a global trending list.
    movie           Show the trending movies in the results.
    tv              Show the trending TV shows in the results.
    person          Show the trending people in the results.

    Valid Time Windows
    Time Window     Description
    day             View the trending list for the day.
    week            View the trending list for the week.

    required:
    optional:
    '''

    return _call('GET', f'https://api.themoviedb.org/3/trending/{media_type}/{time_window}')
