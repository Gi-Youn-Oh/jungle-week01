# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
# 예제 입력 1
# 8
# 예제 출력 1
# 92
import sys
N = int(sys.stdin.readline())
row = [0] * N
count = 0
def find_queen(x):
    global count
    if x == N:
        count += 1
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                find_queen(x+1)
def check(y):
    for j in range(y):
        if row[y] == row[j] or abs(row[y] - row[j]) == abs(y-j):
            return False
    return True
find_queen(0)
print(count)