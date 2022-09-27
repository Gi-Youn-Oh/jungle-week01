# import sys

# N = int(sys.stdin.readline().split()[0])

# nums = list(map(int,sys.stdin.readline().split()))
# ordered_nums = []

# # 넣으면서 크기순으로 정렬? > 안됨. 문제 조건이 그렇게 못하게 해놓음 > 따로 정렬하는 파트 만들어야됨.

# # 크기순 정렬
# for i in range(N):
#     num = nums[i]
#     for j in range(len(ordered_nums)):
#         if num < ordered_nums[j]:
#             ordered_nums.insert(j, num)
#             break
#     else:
#         ordered_nums.append(num)
    
# if len(ordered_nums) == 3:
#     print(ordered_nums[2] * 2 - ordered_nums[1] - ordered_nums[0])
# else:
#     linked_li = [ordered_nums[-2], ordered_nums[0], ordered_nums[-1]]

#     prev = 0
#     last_idx = 2 # last_idx 인덱스는 계속 갱신이 필요함.
#     max_sum = abs(linked_li[0] - linked_li[1]) + abs(linked_li[1] - linked_li[2])

#     if len(ordered_nums) % 2 == 0:
#         for n in range(1, len(ordered_nums) - 2):
#             prev_dif = abs(linked_li[0] - ordered_nums[n])
#             last_dif = abs(linked_li[last_idx] - ordered_nums[n])

#             if prev_dif > last_dif:
#                 linked_li.insert(0,ordered_nums[n])
#                 max_sum += prev_dif
#             else:
#                 linked_li.append(ordered_nums[n])
#                 max_sum += last_dif
            
#             last_idx += 1 # last_idx 인덱스 갱신
#     else:
#         for n in range(1, len(ordered_nums) - 2):
#             prev_dif = abs(linked_li[0] - ordered_nums[n])
#             last_dif = abs(linked_li[last_idx] - ordered_nums[n])

#             if prev_dif > last_dif:
#                 linked_li.insert(0,ordered_nums[n])
#                 max_sum += prev_dif
#             else:
#                 linked_li.append(ordered_nums[n])
#                 max_sum += last_dif            
#             last_idx += 1 # last_idx 인덱스 갱신
#     print(max_sum, linked_li)




# 리스트 전역변수, 지역변수 개념
# li = [0,1,2,3]

# def func():
#     li = [1]
#     li[0] = 2
#     print('in func',li)

# func()
# print(li)


s1 = set([1,2,3])
print(len(s1))
s2 = set()
print(s1,s2)