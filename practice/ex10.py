n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] < x :
        print(a[i], end=" ")



# # list a가있다.
# a = [0, 1]
# a.append(30)
# a
# [0,1,30]
# # append 는 요소 추가 

# a = [0, 1]
# a.insert(30)
# a
# [0,1,[30]]
# #insert 는 리스트안에 리스트 추가

# a =[0,1,30]
# a.pop()
# >
# a=[0,1]
# .pop() 은 마지막 요소 삭제

# a =[0,1,30]
# a.remove(1)
# >
# a=[0,30]
# . remove(특정요소) 특정요소 삭제