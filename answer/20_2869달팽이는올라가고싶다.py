# a,b,v = map(int, input().split())

# day = 0
# snail_height = 0
a,b,v = map(int, input().split())
day=(v-a)//(a-b)

snail_height = (a-b)*day
while True:
    day += 1
    snail_height += a
    if snail_height >= v:
        break
    snail_height -= b
print(day)

# a,b,v = map(int, input().split())
# day=(v-a)//(a-b)

# for _ 
# snail_height = (a-b)*day
# if snail_height + a <= v:
#     day += 1

# print(day)


    # a+(-b)
    # day=v/(a-b)
    # if a+(-b)>=v :
    #     print(day)
    #     break