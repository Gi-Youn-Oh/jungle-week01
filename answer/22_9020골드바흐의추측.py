# # 1. 지문 읽기 및 컴퓨터적 사고
# # 2. 요구사항(복잡도) 분석
# # 3. 문제 해결을 위한 아이디어 찾기
# # 4. 소스코드 설계 및 코딩

# 1. 테스트 개수 받기
# 2. 짝수 N 받기 >> 조건 짝수만 / 홀수 x
# 3. 짝수 n 에 대한 파티션 출력 / 파티션  : 짝수n = 소수 + 소수 /
# 4. 소수는 작은 것 부터 출력 / 공백으로 구분 / 파티션 여러가지일 경우에는 두 소수의 차이가 가장 작은 것으로
# --
# 요구 사항
# 1. 짝수 n 에대한 파티션 출력
# 2. 출력시 소수 작은 것부터
# 3. 공백으로 소수 구분
# 4. 파티션 여러가지일 경우 소수차이가 가장 작은 것으로 출력
# ---
# 아이디어
# 짝수 를 받을 때 조건문으로 짝수만 받도록 아니면 다시입력하도록하기 / 짝수를 받는다고했으니까 별도 조건 없어도 될듯
# 짝수 n 의 리스트화 ex ) 8 > [ 1, 2, 3, 4, 5, 6, 7, 8]
# 리스트 중에서 소수찾기 21 활용
# [2, 3, 5, 7]
# 소수중에서 차이가 작은 수 꺼내기 조건문 > 소수 리스트 중에서 리스트 1 +리스트 2 = 짝수 n 이면서,
# 공백으로 소수 구분 > sep= ' '

T = int(input())

for _ in range(T):
    n = int(input())
    pull_list = list()
    for i in range(1, n+1):
        pull_list.append(i)

# print(pull_list)
    sosu_list = []
    for so in pull_list:
        for i in range(2, so):
            if so % i == 0:
                break
        else:
            if so == 1:
                pass
            else:
                sosu_list.append(so)

    for i in range(len(sosu_list)//2, -1,-1):
        if n - sosu_list[i] in sosu_list:
            if sosu_list[i] > n - sosu_list[i]:
                print(n-sosu_list[i], sosu_list[i])
            else:
                print(sosu_list[i],n-sosu_list[i])
            break


