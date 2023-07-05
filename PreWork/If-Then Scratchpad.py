year = 2004

def is_leap_year(a_year):
    if (a_year % 400 == 0) and (a_year % 100 == 0):
        return True
    elif (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    else:
        return False


print(is_leap_year(year))
