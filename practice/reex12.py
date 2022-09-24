T = int(input()) # 테스트 개수 주어짐

for _ in range(T): # 테스트 개수만큼 문자열 받기
    sentence = list(input()) # ['o', 'o', 'x' 분열]
    score = 0
    sum_score = 0

    for i in sentence: 
        if i == 'O':
            score +=1
            sum_score +=score
        else : 
            score = 0
    print(sum_score)


# 구할 값 생각하기 > 점수를 구하시오 > 점수 > sum_score로 정의 / 문장당 값 = sum 
# 스코어는 더해지기 때문에 최초값을 0으로 설정

# 점수는 문자 o가 있을때 1을 더한다 
# 연속되면 o에 더하고 아니면 멈춘다.
# 반복 > o 가 연속이면 +1 