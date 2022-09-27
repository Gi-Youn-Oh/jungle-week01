import sys

heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline())) # 한줄에 여러 입력 값 

total = sum(heights)
one = 0
two = 0

for i in range(9):           # 반복문을 통해 인덱스 각각의 값 계산하기 숙달필요
    for j in range(i+1, 9):
        if total - (heights[i] + heights[j]) == 100:
            one, two = heights[i], heights[j]
            break

heights.remove(one)
heights.remove(two)
heights.sort() # 오름차순 정렬

# 출력
for i in heights:
    print(i)



# 방법1
heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline())) # 한줄에 여러 입력 값 

# 방법2
data = lambda: sys.stdin.readline().rstrip() # 오른쪽 공백 삭제
heights = [int(data()) for _ in range(9)]
## 함수를 딱 한 줄로 만들게 해주는 lambda
## lambda 매개변수 : 표현식

# 방법3
heights = [int(input()) for i in range(9)]    

from itertools import combinations

heights = [int(input()) for _ in range(9)]
occation = list(combination(hieights,7)) #9개중에 7개만 선택하는 조합 저장하기

for i in occation:
	if sum(i) is 100:a
    	answer = list(i) # 합이 100이면, list로 저장하기
    	break

answer.sort()
for i in answer:
	print(i)