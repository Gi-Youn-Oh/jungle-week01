n = int(input())
so_list = list(map(int, input().split()))

sum = 0
for so in so_list:
    for i in range(2,so):
        if so % i == 0: 
            break
    else :
        if so != 1:
            sum +=1
print(sum)

