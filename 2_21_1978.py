import sys

def is_prim_num(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    print(num,end=' ')
    return True

N = int(sys.stdin.readline().split()[0])

nums = list(map(int,sys.stdin.readline().split()))
cnt = 0
for num in nums:
    if(is_prim_num(num)):
        cnt += 1
print()
print(cnt)