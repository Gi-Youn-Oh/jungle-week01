import itertools

n = int(input())
arr = list(map(int, input().split()))
print(arr)
arr.sort()
print(arr)
arr2 = list(itertools.permutations(arr, n))
print(arr2)