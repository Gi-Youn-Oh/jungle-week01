def here_to_there(n, here, there, Debug=True):
    if n == 1 and Debug == True:
        print(here, there)
    else:
        some_where = 6 - here - there
        here_to_there(n-1, here, some_where)
        here_to_there(1, here, there)
        here_to_there(n-1, some_where, there)


n = int(input())

if n > 20:
    print(2**n - 1)
    # here_to_there(n, 1, 3, False)dfdf
else:
    print(2**n - 1)
    here_to_there(n, 1, 3, True)
