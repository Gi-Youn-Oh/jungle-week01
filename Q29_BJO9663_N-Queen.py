
N = int(input())
flag = [False] * N
flag_b = [False] * ((2 * N)-1)
flag_c = [False] * ((2 * N)-1)
pos = [0] * N
count = [0]


def set(i):
    for j in range(N):
        if (not flag[j]) and (not flag_b[i+j]) and (not flag_c[N-1-j+i]):
            pos[i] = j
            if i == (N-1):
                count[0] += 1
            else:
                flag[j] = True
                flag_b[j+i] = True
                flag_c[N-1-j+i] = True
                set(i+1)
                flag[j] = False
                flag_b[j+i] = False
                flag_c[N-1-j+i] = False


set(0)
print(count[0])
