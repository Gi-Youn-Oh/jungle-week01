nums = input().split()

num_list = { 'x':int(nums[0]), 'y':int(nums[1]), 'w':int(nums[2]), 'h':int(nums[3]) }

x = int(nums[0])
y = int(nums[1])
w = int(nums[2])
h = int(nums[3])

print(min(w-x,x,h-y,y))