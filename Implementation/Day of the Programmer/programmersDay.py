def solve(year):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 256

    if (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        months[2] = 29

    if year == 1918:
        day = day + 13

    for i, month in enumerate(months):
        if day > month:
            day -= month
        elif day <= month:
            month = i
            break

    return '{:02d}.{:02d}.{}'.format(day, month, year)
