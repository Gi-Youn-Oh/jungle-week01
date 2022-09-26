from operator import truediv
from sys import stdin, stdout


def pick(order):
    if order == 3:
        s.add(''.join(map(str, li)))
        return
    for i in range(n):
        if check[i]:
            continue
        li.append(nums[i])
        check[i] = 1
        pick(order+1)
        li.pop()
        check[i] = 0

# 새로운 합이 sum보다 더 작은가요?


def min_checker(min, sum):
    # return true if sum is smaller
    if min > sum:
        return True
    else:
        return False


how_many, target_num = map(int, stdin.readline().split())
nums = list(map(int, input().split()))
nums.sort()
print(nums)

flag = False
for i in range(how_many):
    for j in range(i+1, how_many):
        for k in range(j+1, how_many):
            sum = nums[i]+nums[j]+nums[k]
            # break 조건
            if sum > target_num:
                flag = True
                break
            else:
                answer = sum

        if flag:
            break
    if flag:
        break

print(answer)
