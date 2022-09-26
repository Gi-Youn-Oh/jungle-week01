from sys import stdin

N = int(stdin.readline().split()[0])
W = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 제대로 들어가는 지 확인
# for i in range(N):
#     for j in range(N):
#         print(f'{W[i][j]:3}', end=' ')
#     print()
