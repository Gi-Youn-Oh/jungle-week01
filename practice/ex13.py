c = int(input())
for _ in range(c):
    ex = list(map(int, input().split())) # 인원수 점수 5개 / but 한줄을 인원 점수 상관없이 하나의 리스트로 만든다.
    # ex[0] = 인원수
    # ex[1:] = 각 점수
    avg = sum(ex[1:])/ex[0] # 점수 평균
    ace = 0 # 점수 평균을 넘는 학생 수
    for i in ex[1:]:
        if i > avg :
            ace +=1  
        rate = ace/ex[0]*100 # 평균이상학생수의 비율 
    print(f'{rate:.3f}%')

