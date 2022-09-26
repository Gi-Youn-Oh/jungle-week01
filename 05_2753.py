year = int(input())

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 != 0:
                print(1)
                return
        if year % 400 == 0:
            print(1)
            return
    print(0)

is_leap_year(year)