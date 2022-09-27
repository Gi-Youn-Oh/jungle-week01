N, r, c = map(int, input().split())
grid = [0, 0]


def where_is_it(x, y):
    if (x == True) and (y == True):
        return 3
    elif (x == False) and (y == True):
        return 2
    elif (x == True) and (y == False):
        return 1
    elif (x == False) and (y == False):
        return 0


def position_checker(x, y, n):
    if x >= grid[0] + 2**(n-1):
        x = True
        grid[0] += 2**(n-1)
    else:
        x = False

    if y >= grid[1] + 2**(n-1):
        y = True
        grid[1] += 2**(n-1)
    else:
        y = False
    return x, y


answer = 0
while N > 0:
    checked_x, checked_y = position_checker(c, r, N)
    answer += where_is_it(checked_x, checked_y) * (2 ** (2*N-2))
    N -= 1

print(answer)
