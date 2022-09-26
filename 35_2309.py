import sys

dwalf_heights = []
dwalf_list = []

sum_of_dwalf = 0
num_of_dwalf = 7
all_num_of_dwalf = 9

not_her_dwalf_1 = -1
not_her_dwalf_2 = -1

## 정렬하면서 입력받기 - 거의 O(1)
for i in range(all_num_of_dwalf):
    height = int(sys.stdin.readline().split()[0])
    for j in range(len(dwalf_heights)):
        if dwalf_heights[j] > height:
            dwalf_heights.insert(j,height)
            break
    else:
        dwalf_heights.append(height)
    sum_of_dwalf += height

# for i in range(num_of_dwalf):
#     sum_of_dwalf = 0
#     for d1 in range(all_num_of_dwalf):
        

print(dwalf_heights,sum_of_dwalf)


for i in range(all_num_of_dwalf):
    for j in range(i,all_num_of_dwalf):
        if dwalf_heights[i]+dwalf_heights[j] == sum_of_dwalf - 100:
            not_her_dwalf_1 = i
            not_her_dwalf_2 = j
            break
    if not_her_dwalf_1 > 0:
        break


pre_sum = 0
for i in range(all_num_of_dwalf):
    if i != not_her_dwalf_1 and i != not_her_dwalf_2:
        dwalf_list.append(dwalf_heights[i])
        pre_sum += dwalf_heights[i]

print(dwalf_list,pre_sum)
# [print(d) for d in dwalf_list]
