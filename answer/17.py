# n = int(input())

# for _ in range(n):
#     cnt, word = input().split()
#     for x in word:
#        print(x*int(cnt), end='') # end='' 옆으로 붙임
#     print() # 줄넘김

# T = int(input())

# for _ in range(T):
#     r, abc = input().split()
#     r = int(r)

#     print((abc[i])*len(abc), end='')
T = int(input())

for _ in range(T):
    r, abc = input().split()
    r = int(r)
    for i in abc:
        print(i*r,end='')
    print()


# r = int(input())
# abc = input()
# for i in abc:
#     print(i*r, end='')

# 2, 'abc'
# for i in 'abc':
#     print(i*2, end='')

# 5, '/HTP'
# for i in 'HTP':
#     print(i*5,end='')

# for i in range(4):
#     print(i)
# print()
# for i in [1,4,2,3]:
#     print(i)
