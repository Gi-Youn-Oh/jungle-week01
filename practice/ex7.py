n= int(input())
for i in range(1,10):
    print(n,'*',i,'=', n*i)

# range 함수

# range(10)
# > range(0,10) / 즉 0부터 9까지

# list(range(10))
# > [0,1,2,3,4,5,6,7,8,9] 리스트 인덱스 안에 0~9까지

# list(range(0,20,2))
# > [0,2,4,6,8,10,12,14,16,18] 리스트 인덱스 2단위 

# for i in range(10, -1, -1):
#     print (i)

# 10
# 9
# 8
# 7
# ..
# 0 