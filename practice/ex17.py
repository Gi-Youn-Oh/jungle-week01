T = int(input()) # 테스트 개수 받기

for _ in range(T):
    n, abc = input().split() # 반복회수, 문자열 받기
    n = int(n)            # 반복회수 정수화
    for i in abc:
        print(i*n, end="")  #'a'*3= aaa / end = "" 줄바꿈없이 이어서 / sep = '' > separation 분리
    print() #줄넘김
