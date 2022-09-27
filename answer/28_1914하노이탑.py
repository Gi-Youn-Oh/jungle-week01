#1. 원판의 개수 받기

n = int(input())

# 원판 개수를 각각의 원판으로 나누어 리스트화 받기
num = []
for i in range(1,n+1) :
    num.append(i)
print(num)

a = []
b = []
c = []

# 출력 수행과정 수 > 원판 이동할때마다 count +1 
# 1 2 3  나무판 넘버 / 1 2 3 .. n 원판넘버  이