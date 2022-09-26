from operator import truediv
from sys import stdin, stdout


how_many, target_num = map(int, stdin.readline().split())
nums = list(map(int, input().split()))
nums.sort()
min = 300000

flag = False
for i in range(how_many):
    for j in range(i+1, how_many):
        for k in range(j+1, how_many):
            sum = nums[i]+nums[j]+nums[k]
            judge = target_num - sum
            if judge == 0:
                answer = sum
                flag = True
                break
            elif judge < 0:
                break
            elif judge < min:
                min = judge
                answer = sum
        if flag:
            break
    if flag:
        break

print(answer)
