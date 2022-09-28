from sys import stdin

# def put(n:int, cnt:int) -> None:
#     """각 열에 배치한 퀸의 위치를 출력"""
    
#     # for i in range(n):
#     #     # print(f'{queen_i[i]:2}', end='')
#     #     print(f'{queen_i[i]:2}', end='')

#     # print()
#     cnt += 1

n = int(stdin.readline().split()[0])

queen_i = [0]*n
queen_j = [False]*n
queen_rightup = [False]*(2*n-1)
queen_rightdown = [False]*(2*n-1)
cnt = [0]

def pos_queen(i:int, n:int) -> None:
    """i열에 퀸을 배치"""
    for j in range(n):
        if not queen_j[i]:
            if not queen_rightdown[i+j]:
                if not queen_rightup[i-j+n-1]:
                    queen_i[i] = j
                    if i == n-1:
                        # put(n)
                        cnt[0] += 1
                    else:
                        queen_j[i] = queen_rightup[i+j]= queen_rightdown[i-j+n-1] = True
                        pos_queen(i+1,n)
                        queen_j[i] = queen_rightup[i+j]= queen_rightdown[i-j+n-1] = False
pos_queen(0,n)
# 큰 문제를 작은 문제로 분할하고, 작은 문제 풀이법을 결합하여 전체 풀이법을 얻는 방법을 분할 정복법(분할 해결법)이라 함.


print(cnt)