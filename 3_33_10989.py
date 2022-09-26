import sys

N = int(sys.stdin.readline().split()[0])
nums = [0]*10001
cnt = 0


for _ in range(N):
    num = int(sys.stdin.readline().split()[0])
    nums[num] += 1
print()
for i in range(10001):
    for j in range(nums[i]):
        print(i)
        cnt += 1
    if cnt == N:
        break