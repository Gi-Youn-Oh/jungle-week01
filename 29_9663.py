from sys import stdin


def put(n:int) -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    cnt = 0
    for i in range(n):
        # print(f'{queen_i[i]:2}', end='')
        cnt += 1
    print(cnt)

def set_queen(i:int, n:int) -> None:
    """i열에 퀸을 배치"""
    for j in range(n):
        if not queen_j[i]:
            if not queen_rightdown[i]:
                if not queen_rightup[i]:
                    queen_i[i] = j
                    if i == n-1:
                        put(n)
                    else:
                        for k in range(i, -1, -1):
                            queen_rightup[k] = True
                        for k in range(i,n):
                            queen_rightdown[k] = True
                        queen_j[i] = True
                        set_queen(i+1,n)
                        queen_j[i] = False
                        for k in range(i, -1, -1):
                            queen_rightup[k] = False
                        for k in range(i,n):
                            queen_rightdown[k] = False
# 이렇게 차례대로 가지가 뻗어 나가듯이 배치 조합을 열거하는 방법을 분기 작업이라 함.
# 쿤 문제를 작은 문제로 분할하고, 작은 문제 풀이법을 결합하여 전체  풀이법을 얻는 방법을 분할 정복법(분할 해결법)이라 함.

n = int(stdin.readline().split()[0])

# 이렇게 함으로써 열에 하나씩 퀸을 둘 수 있게 됨.
queen_i = [0]*n
queen_j = [False]*n
queen_rightup = [False]*n
queen_rightdown = [False]*n
set_queen(0,n)