#!/usr/bin/env python3
class Time:
   """Simple object type for time of the day.
      Data attributes: hour, minute, second
   """
   def __init__(self, hour=12, minute=0, second=0):
       """Constructor for Time object""" 
       self.hour = hour
       self.minute = minute
       self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'
def sum_times(t1, t2):
    """Add two time objects and return the sum with proper carry-over."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # Handle carry-over for seconds
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second %= 60

    # Handle carry-over for minutes
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute %= 60

def valid_time(time):
    if time.hour < 0 or time.hour >= 24:
        return False
    if time.minute < 0 or time.minute >= 60:
        return False
    if time.second < 0 or time.second >= 60:
        return False
    return True

def change_time(time, seconds):
    time.second += seconds

    # Handle negative seconds and roll over minutes
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    
    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    # Handle negative minutes and roll over hours
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    # Handle hours that go out of range (24-hour format)
    if time.hour < 0:
        time.hour += 24
    elif time.hour >= 24:
        time.hour -= 24

    return None

