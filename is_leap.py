def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    elif year % 3200 != 0:
        return True
    else:
        return False

is_leap(2001)
