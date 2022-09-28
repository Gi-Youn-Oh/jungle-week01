from sys import stdin, stdout
from itertools import permutations

def sum_dif(A:list) -> int:
    ans_sum = 0
    for i in range(len(A)-1):
        ans_sum += abs(A[i+1]-A[i])
    return ans_sum

N = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().split()))

all_permutations = list(permutations(nums,N))

max_sum = 0
for p in all_permutations:
    if max_sum < sum_dif(list(p)):
        max_sum = sum_dif(list(p))

print(max_sum)