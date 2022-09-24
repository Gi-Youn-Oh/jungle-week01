import sys

# def is_arithmetical(num):
#     interval = abs(num%10 - (num//10)%10)
#     while num > 10:
#         num = num//10
#         pre_interval = abs(num%10 - (num//10)%10)
#         if pre_interval == interval:


Num = int(sys.stdin.readline().split()[0])
cnt = 0
for N in range(1, Num+1):
    len_ofN = len(str(N))
    num = N
    interval_list = [0]*(len_ofN-1)
    for i in range(len_ofN - 1):
        interval = N%10 - (N//10)%10
        interval_list[i] = interval
        N = N//10
    for i in range(1,len_ofN - 1):
        if interval_list[i] != interval_list[i-1]:
            break
    else:
        cnt += 1
        # print(num,'-',interval_list,cnt)
print(cnt)
