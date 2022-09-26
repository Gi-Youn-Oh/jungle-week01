A = int(input())
B = int(input())
C = int(input())

N = A*B*C
N = str(N)

for i in range(0, 10):
    cnt = 0
    pre_num = str(i)
    for j in range(len(N)):
        if pre_num == N[j]:
            cnt += 1
    print(cnt)
