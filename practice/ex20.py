a, b, v = map(int, input().split())
day = (v-a)//(a-b) # 거리 = 시간 * 속력 / (a-b)*day + a = v
walk = (a-b)*day  # 초기값을 0에 두는 것이 아닌 계산된 시작점을 설정해주어 시작한다.
while walk < v:
        walk+=a
        day+=1
        if walk < v :
            walk -=b
        else:   
            print(day)

# a,b,v = map(int, input().split())
# day=(v-a)//(a-b)

# snail_height = (a-b)*day
# while True:
#     day += 1
#     snail_height += a
#     if snail_height >= v:
#         break
#     snail_height -= b
# print(day)
