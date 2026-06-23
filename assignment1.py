#!/usr/bin/env python3

"""
OPS445 Assignment 1
Program: assignment1.py
Author: Dilpreet Kaur
Semester: Summer 2026
"""

import sys


def day_of_week(year: int, month: int, date: int) -> str:
    """Return day of week using Tomohiko Sakamoto algorithm."""
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3,
              7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400
           + offset[month] + date) % 7
    return days[num]


def leap_year(year: int) -> bool:
    """Return True if the year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def mon_max(month: int, year: int) -> int:
    """Return maximum number of days for the given month."""
    if month == 2:
        if leap_year(year):
            return 29
        return 28

    month_days = {
        1: 31, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return month_days[month]


def after(date: str) -> str:
    """Return the next date in YYYY-MM-DD format."""
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    day += 1

    if day > mon_max(month, year):
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    return f"{year}-{month:02}-{day:02}"


def usage():
    """Print usage message and exit."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)


def valid_date(date: str) -> bool:
    """Return True if the date is valid YYYY-MM-DD."""
    if len(date) != 10:
        return False

    if date[4] != '-' or date[7] != '-':
        return False

    year, month, day = date.split('-')

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True


def day_count(start_date: str, stop_date: str) -> int:
    """Return number of weekend days between two dates, inclusive."""
    count = 0
    current_date = start_date

    while current_date <= stop_date:
        year, month, day = current_date.split('-')
        weekday = day_of_week(int(year), int(month), int(day))

        if weekday == 'sat' or weekday == 'sun':
            count += 1

        current_date = after(current_date)

    return count


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    first_date = sys.argv[1]
    second_date = sys.argv[2]

    if not valid_date(first_date) or not valid_date(second_date):
        usage()

    start_date, end_date = sorted([first_date, second_date])

    weekends = day_count(start_date, end_date)

    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")
