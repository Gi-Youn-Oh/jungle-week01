# import sys
# input = sys.stdin.readline

# n = int(input())

# num_list = []

# for i in range(n):
#     num_list.append(int(input()))

# num_list1=sorted(num_list)
# for i in sorted(num_list):
#     print(i)

import sys

N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())
    
    check_list[input_num] = check_list[input_num] + 1  #인덱스 값 0 > 1로 해당 번째 수 숫자 11이면 인덱스 11번째 수를 1로 11이 1개있다로 인식
    
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):   # 0이면 출력 x 1이면 해당 인덱스 넘버 즉 입력 수가 1개 출력 
            print(i)

# 핵심 
# 메모리 데이터 줄이기 위해 데이터 값 먼저 범위로 선정

# 리스트를 만들어 인덱스 값 자체로 해당 수의 개수를 정한다.

# 리스트의 인덱스 넘버 = 입력 수 로 정렬 시켜 해당 개수만큼 출력