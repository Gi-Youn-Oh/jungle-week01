a, b = input().split()

a=int(a[::-1])
b=int(b[::-1])

if a>b:
    print(a)
else:
    print(b)

# reverse 
# a= ['a','b','c']
# a.reverse()
# a
# ['c','b','a']
# [시작점:끝점:step]
# step 2 > 0 2 4 6 8 / a[0:9:2]
# step -1 > 5 4 3 2 1 / b[5:0:-1]