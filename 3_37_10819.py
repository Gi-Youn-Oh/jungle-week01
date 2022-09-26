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
#             ordered_nums.insert(j+1, 0)
#             break
#     else:
#         ordered_nums.append(num)
#         ordered_nums.append(0)

# # 0인 값들을 바꿔주기
# for i in range(N):
#     back_idx = -i-1
#     if ordered_nums[i] == 0:
#         ordered_nums[i] = ordered_nums[back_idx]
#         # print(back_idx, ordered_nums[i],ordered_nums[back_idx])
# print(ordered_nums)
# max_sum = 0
# past_num = ordered_nums[0]
# for i in range(1, N):
#     pre_dif = ordered_nums[i]-past_num
#     max_sum = max_sum + abs(pre_dif)
#     past_num = ordered_nums[i]
# print(max_sum)

import sys

N = int(sys.stdin.readline().split()[0])
nums = list(map(int,sys.stdin.readline().split()))

