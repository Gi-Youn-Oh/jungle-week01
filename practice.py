from itertools import permutations

import sys
input= sys.stdin.readline

n= int(input())

per= list(permutations([(i) for i in range(n)], n))
temp=[]
for i in range(n):
    temp.append(list(map(int,input().split())))

result= 10**10

for i in range(len(per)//n): #같은게 있음
    result_tem = 0 
    judge= True
    for j in range(n):
        if temp[(per[i][j])-1][(per[i][(j+1)%n])-1] == 0:
            judge= False
        result_tem += temp[(per[i][j])-1][per[i][(j+1)%n]-1]
    if result_tem < result and judge:
        result= result_tem
print(result)
