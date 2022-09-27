#1. 원판의 개수 받기

n = int(input())

# 원판 개수를 각각의 원판으로 나누어 리스트화 받기
num1 = []
for i in range(1,n+1) :
    num1.append(i)
print(num1)

num1 = [5] # 나무판 1
num2 = [4] # 나무판 2
num3 = [7] # 나무판 3

#나무판 1>3으로 이동시켜야하는데 각 판에서 나무판1 의 인덱스 값이 나무판 2 or 나무판3 의인덱스 값보다 작을때 이동하도록 조건 달기 반복시키기
#재귀 탈출 조건 나무판 1,2가 리스트가 없을때 끝난다  
# 출력 수행과정 수 > 원판 이동할때마다 count +1 
# 1 2 3  나무판 넘버 / 1 2 3 .. n 원판넘버  이

def move(no: int, x : int, y :int) -> None:
    # 원바 no개를 x에서 y기둥으로 옮김
    if no > 1 :
        move(no-1, x, 6-x-y)

    print(f"원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.")

    if no > 1:
        move(no-1, 6-x-y, y)

n = int(input())  # 원반 개수 받기

move(n, 1, 3)