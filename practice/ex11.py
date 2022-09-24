numbers=[] # 빈 list 만들기s / number=list()
for _ in range(9): #9개의 정수를 받아서 리스트에 입력
    i=int(input())
    numbers.append(i) # list.append() list에 index값 춫가
print(max(numbers)) #max(list) list 의 최댓값
print(numbers.index(max(numbers))+1) # index 넘버는 0부터 시작하기에 1추가
