#!/usr/bin/env python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def time_to_sec(time):
    '''Convert a time object to a single integer representing the number of seconds from midnight.'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''Convert a given number of seconds to a time object in hour:minute:second format.'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(time1, time2):
    '''Returns the sum of two time objects.'''
    seconds1 = time_to_sec(time1)
    seconds2 = time_to_sec(time2)
    total_seconds = seconds1 + seconds2
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    '''Adds or subtracts seconds from a time object and adjusts the time accordingly.'''
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None

def format_time(t):
    '''Returns the time in hour:minute:second format.'''
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

