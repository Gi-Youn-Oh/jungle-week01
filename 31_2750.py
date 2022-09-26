import sys

N = int(sys.stdin.readline().split()[0])

nums = []

for _ in range(N):
    pre = int(sys.stdin.readline().split()[0])
    for i in range(len(nums)):
        if pre < nums[i]:
            nums.insert(i,pre)
            break
    else:
        nums.append(pre)
for num in nums:
    print(num)