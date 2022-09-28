from sys import stdin, stdout

# N = int(stdin.readline().split()[0])

# S = [stdin.readline().split()[0] for _ in range(N)]
N = 13
S = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

S=list(set(S))
S.sort()
S.sort(key=len)


[stdout.write(s + '\n') for s in S]