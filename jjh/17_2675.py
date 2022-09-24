import sys

T = int(sys.stdin.readline().split()[0])

for _ in range(T):
    N, S = sys.stdin.readline().split()
    N = int(N)
    for i in range(len(S)):
        # print(S[i]*N,end='')
        sys.stdout.write(S[i]*N)
    sys.stdout.write('\n')
