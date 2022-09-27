from operator import truediv
from sys import stdin, stdout

##initializing##
how_many = int(stdin.readline())
nums = list(map(int, input().split()))
flag = [False] * how_many
pos = [0] * how_many


def abs_diff(a, b):
    return abs(a - b)


def set(i):
    for j in range(how_many):
        if not flag[j]:
            pos[i] = nums[j]
            if i == (how_many-1):
                answer_sheet.append(calculate(pos, how_many))
            else:
                flag[j] = True
                set(i+1)
                flag[j] = False


def calculate(arr, num):
    sum = 0
    for i in range(len(arr)-1):
        sum += abs_diff(arr[i], arr[i+1])
    return sum


#run#
answer_sheet = []
set(0)
print(max(answer_sheet))
