# abs 
# abs(-99) = 99 절대값 

# permutation 순열 
# import itertools

# arr = ['A', 'B', 'C']
# nPr = itertools.permutations(arr, 2)
# print(list(nPr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]


# from re import L
# import sys  
# import itertools
# input = sys.stdin.readline

# n = int(input())

# array = list(map(int,input().split()))

# array_per = list(itertools.permutations(array,2))

# print(array_per)

# def absolute(li):
#     total = 0
#     for i in range(len(li)-1):
#         total += abs(li[i]-li[i+1])
#     return total


import itertools

n = int(input())
arr = list(map(int, input().split()))
# arr.sort()
arr2 = list(itertools.permutations(arr, n))
res = 0
for i in range(len(arr2)):                          # 비교값 현재와 결과값을 0 으로 초기값 설정
    cur = 0                                         # 현재값을 계속 받아서 결과값에 대입해주고 대입한결과값을 또 결과값이랑 비교 이전값과 새로운값을 비교 
    for j in range(0, n - 1):                       # 순회가 끝나면 최종적으로 남은 수가 조건의 최대치 값이다.
        cur += abs(arr2[i][j] - arr2[i][j + 1])     # 인덱스의 인덱스 값을 구한다 
                                                    # 차이의 최댓값을 구하는 것이아닌 각 차이의 합의 최댓 값을 구하는 것이므로 모든 순열을 확인해야한다.
    if cur > res:
        res = cur
print(res)