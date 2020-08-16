def readable_timedelta(days):
    '''
     this function Return a string of the number of weeks and days included in days.

    argument:
    days -- number of days to convert (integer)

    Returns:
    string of the number of weeks and days included in days
    '''
    # insert your docstring here

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
