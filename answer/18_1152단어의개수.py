# word = input().split()
# print(len(word))

# The Curious Case of Benjamin Button > word 
# input () 하면 그대로 여기서 .split() 하면
# [The, Curious, Case, of, Benjamin, Button]
# word 의 길이 즉 개수 = len(word)
s1, s2, s3, s4, s5, s6 =  input().split()

# 1 2 3 4 5 6
# '1' '2' '3' '4' '5' '6'
map(int, input().split())


map(int, ['1','2','3','4','5','6'])
int('1'), int('2')

n1, n2, n3, n4, n5, n6 = map(int, ['1','2','3','4','5','6'])
n1, n2, n3, n4, n5, n6 = int('1'), int('2'), int('3'), int('4'), int('5'),int('6')
# n1 = 1 ... n6 = 16
print(s1,s2,s3,s4,s5,s6)
# >[ [The], [Curious], [Case], [of], [Benjamin], [Button]]