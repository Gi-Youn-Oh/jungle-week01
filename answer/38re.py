from itertools import permutations
import sys
city_number = int(sys.stdin.readline()) # 도시의 개수
input_matrix = []   # 도시 루트 경우의수
city_list = []      # 
for i in range(city_number):
    input_matrix.append(list(map(int, sys.stdin.readline().split())))
    city_list.append(i)
inf = float("inf")
min = inf
permutations_group = permutations(city_list, city_number)
def calculate_cost(matrix, list_case, city_number):
    count = 0
    for i in range(0, city_number-1):
        cost = matrix[list_case[i]][list_case[i+1]]
        if cost == 0:
            count = inf
            break
        else:
            count += cost
    cost = matrix[list_case[city_number-1]][list_case[0]]
    if cost != 0:
        count += cost
    else:
        count = inf
    return count
for case in permutations_group:
    list_case = list(case)
    total_count = calculate_cost(input_matrix, list_case, city_number)
    if total_count < min:
        min = total_count
print(min)




