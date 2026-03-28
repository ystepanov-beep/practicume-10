def is_leap(year: int) -> bool:
    """Return True if the given year is a leap year."""
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def months_leap(is_leap) -> list:
    """Return a list with the number of days in each month."""

    if is_leap:
        months = [31, 29, 31, 30, 
                  31, 30, 31, 31, 
                  30, 31, 30, 31]
    else:
        months = [31, 28, 31, 30, 
                  31, 30, 31, 31, 
                  30, 31, 30, 31]
    return months


def seconds_counter(time_string: str) -> int:
    """Return the number of seconds passed since 01/01/YYYY 00:00:00."""

    date_part, time_part = time_string.split()
    month, day, year = map(int, date_part.split('/'))
    hour, minute, second = map(int, time_part.split(':'))

    days = sum(months_leap(is_leap(year))[:month - 1]) + day - 1
    return days * 86400 + hour * 3600 + minute * 60 + second


print(seconds_counter(input()))
