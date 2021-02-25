"""
Introduction
Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.
"""


def is_leap_year(year):
    neg_message = f"{year} is not a leap year"
    pos_message = f"{year} is a leap year"
    if year % 400 == 0:
        print(pos_message)
        return True
    if year % 4 == 0 and year % 100 == 0:
        print(neg_message)
        return False
    if year % 4 == 0:
        print(pos_message)
        return True
    print(neg_message)
    return False


is_leap_year(1997)  # Should be false
is_leap_year(1996)  # Should be true
is_leap_year(1900)  # Should be false
is_leap_year(2000)  # Should be true
