from sys import stdin
from itertools import permutations as p

arr = []
n, k = int(stdin.readline()), int(stdin.readline())
for i in range(n):
    arr.append(int(stdin.readline()))
print(arr)
res = set()
for i in list(p(arr, k)): #arr 리스트에 대해서 k 번 순열 만들기 arr 의 요소 4개 로 k개의 배열 arrPk = (arr!/arr-k)! # 모든 순열조합 생성
    print(res)
    res.add(''.join(list(map(str, i))))  #.add 집합에 원소 1개추가 / update 여러개 추가 
print(res)
print(len(res))

# - ''.join(리스트)''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.
# - '구분자'.join(리스트)'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
# '_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

# map(str, i) >  변수 i에 대해서 각각 문자열로 

# >>> a = [1.2, 2.5, 3.7, 4.6]
# >>> a = list(map(int, a))
# >>> a
# [1, 2, 3, 4]

# >>> a = list(map(str, range(10)))
# >>> a
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# from itertools import permutations

# a = [1,2,3]
# permute = permutations(a,2)
# print(list(permute))

# '''
# 결과
# '''

# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]