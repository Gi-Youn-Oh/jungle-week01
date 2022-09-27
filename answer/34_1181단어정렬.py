from re import I
import sys

input = sys.stdin.readline

n= int(input())

word_list = []

for i in range(n):
    word_list.append(input().strip())

set_word_list = set(word_list) # 집합으로 중복 제거
word_list = list(set_word_list) # 집합을 다시 리스트로 

word_list.sort() # abc 순서대로 정렬
word_list.sort(key=len) # 길이 순서대로 정렬

for i in word_list:
    print(i)
