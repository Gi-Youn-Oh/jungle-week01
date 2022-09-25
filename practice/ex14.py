# a = int(input())
# b = int(input())
# c = int(input())

# * list.count(요소) 특정요소가 몇번들어가있는지 셀수 있다.

total = 1
for i in range(3):  # 정수 3개를 받는것을 반복 > 반복문 활용 
    i = int(input())
    total *=i    # 정수 i 3개 곱함
    str_total = str(total) # total 을 문자열로 변환 / ex) a = 'list' > a[0] = l 
# 문자열 끝 문자열에 해당 숫자 개수 구하기 .count

for num in range(10): # 해당 수에 대해서 0~9까지 반복해서 확인
    num_count=str_total.count(str(num))  # 문자열의 문자가 몇개인지를 세야함 문자열에 숫자를 셀수 없다.
    print(num_count)
        