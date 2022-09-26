import sys

N = int(sys.stdin.readline().split()[0])

nums = [0]*2000001
zero = 1000000
minus_end_num = 1000000
plus_end_num = 1000000

for _ in range(N):
    pre = int(sys.stdin.readline().split()[0])
    nums[pre+zero] = 1
    
    if pre+zero > plus_end_num:
        plus_end_num = pre + zero
    elif pre+zero < minus_end_num:
        minus_end_num = pre + zero
    print(pre,pre+zero,plus_end_num,minus_end_num)


for i in range(minus_end_num,plus_end_num+1):
    if nums[i] == 1:
        print(i-zero)