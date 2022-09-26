# 1. 종이의 가로 세로 길이  각 최대 100
x, y = map(int,(input().split()))
# print(x,y) 

# 2. 칼로 잘라야하는 점선의 개수 n 테스트 케이스 n번 반복 
T = int(input())

# 3. 가로 or 세로 n번 자름 가로 = (o xc) / 세로 = (1 yc) 조건 0먼저 입력하면 가로 자르기 1 먼저 입력하면 세로 자르기

for i in range(T):                              # 0먼저 입력하면 자르는 가로 xx 값으로 1먼저 입력하면 자르는 세로 yy값으로  리턴 함수를 만들자
    i = list(map(int, input().split()))
    if i[0] == 0 :
        i[1] = '가로'
        print(i[1])
    elif i[0] == 1:
        i[1] = '세로'
        print(i[1])



    list = [x, y, i[0], i[1]]  # [x ,y , xx , yy]   

for _ in list:                               # 비교 해서 4가지중 제일 큰값을 출력하도록 조건
    if xx > x - xx and yy > y -yy :
        print(xx*xy)
    elif xx > x - xx and yy < y-yy :
        print(xx*y-yy)
    elif xx < x -xx and yy < y-yy:
        print( x*y-yy)
    else :
        print(x*y)


