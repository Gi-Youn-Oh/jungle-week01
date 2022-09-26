
num = list(str(123))
print(num)

# num=list(map(int, str(234)))

# print(num)

# num = int(input())

# num = map(int, str(num))

# pr
# for i in range(1, num+1):
#     num_list = list(map(int, str(i)))

# print(num_list)
#     # if i < 100:
#     #     hansu += 1  # 100보다 작으면 모두 한수
#     # elif num_list[0]-num_list[1] == num_list[1]-num_list[2]


def find(n):
    num_list = []
    for i in range(1,n+1):
        num_list.append(str(i))
    # print(num_list)
        for i in num_list:
            sep = [i[0],i[1],i[2]]
            for i in range(len(sep)):
                sep[i] = int(sep[i])
        han_count = 0 
    for han in new_list:
        if han < 100 :
            han_count +=1
        elif new_list[0]-new_list[1] == new_list[1] - new_list[2]:
            han_count +=1
    return han_count

n = int(input())
print(find(n))   

# def hansu(num) :
#     hansu_cnt = 0
#     for i in range(1, num+1):
#         num_list = list(map(int,str(i)))
#         if i < 100:
#             hansu_cnt += 1  # 100보다 작으면 모두 한수
#         elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
#             hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
#     return hansu_cnt

# num = int(input())
# print(hansu(num))

# def 

# num_list = list(map(int,str(1234)))

# print(num_list)