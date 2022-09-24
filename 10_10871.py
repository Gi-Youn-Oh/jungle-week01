nums = input().split()
N, X = int(nums[0]), int(nums[1])

nums = input().split()

for i in range(N):
    num = int(nums[i])
    if num < X:
        print(num,end=' ')
print()