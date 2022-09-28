from sys import stdin, stdout
from itertools import permutations

how_many = int(input())
values = []
for i in range(how_many):
    value = list(map(int, stdin.readline().split()))
    values.append(value)

all_case = list(permutations([i for i in range(how_many)], how_many))
min_val = 11000000

for k in all_case:
    cost = 0
    error = 0  # 출발 고고, 에러 표시
    for i in range(how_many-1):
        if values[k[i]][k[i+1]] != 0:
            cost += values[k[i]][k[i+1]]
        else:
            error = 1
            break

    if values[k[how_many-1]][k[0]] != 0:
        cost += values[k[how_many-1]][k[0]]
    else:
        error = 1

    if error == 0:
        min_val = min(min_val, cost)

print(min_val)
