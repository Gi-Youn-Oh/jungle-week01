how_many = int(input())

nums = [int(input()) for _ in range(how_many)]
nums.sort()

for i in nums:
    print(i)
