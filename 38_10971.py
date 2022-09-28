from sys import stdin, stdout
from itertools import permutations

# def cost(L:list) -> int:
#     costs_result = 0
#     len_L = len(L)

#     for i in range(len_L):
#         costs_result += W[L[i]][L[(i+1)%len_L]]

#     return costs_result

N = int(stdin.readline().split()[0])
W = [list(map(int, stdin.readline().split())) for _ in range(N)]

possible_permutation = list(permutations([i for i in range(N)], N))
# list(permutations([i for i in range(how_many)], how_many))
min_cost = 11000000

# 원순열임. > (0,1,2,3)(1,2,3,0)(2,3,0,1)(3,0,1,2) 같은 경우임.
for i in range(len(possible_permutation)//N):
    travel_cost = 0

    for j in range(N):
        pre_cost = W[possible_permutation[i][j]][possible_permutation[i][(j+1)%N]]
        if pre_cost == 0:
            break
        travel_cost += pre_cost
    else:
        min_cost = min(min_cost,travel_cost)
    
print(min_cost)
