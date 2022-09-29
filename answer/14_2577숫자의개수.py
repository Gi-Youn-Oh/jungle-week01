# import sys

# a1,a2,a3 = map(int, sys.stdin.readline().split())
# print(a1,a2,a3)
# def asd(n1,n2):
#     return n1+n2
# n11 = asd(3,8)

# a = int(input())
# b = int(input())
# c = int(input())
# a, b, c = map(int, input().split())

# total_str = str(a*b*c)

total = 1
for _ in range(3):
    i = int(input())
    total *= i # 3개의 정수를 곱함
    total_str= str(total) # 숫자를 str 타입으로 변환

for num in range(10): # 0부터 9까지
    num_count =total_str.count(str(num))
    print(num_count)