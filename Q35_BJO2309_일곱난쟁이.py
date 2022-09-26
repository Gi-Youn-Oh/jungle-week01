# def pick(order):
#     if order == k:
#         s.add(''.join(map(str, li)))
#         return
#     for i in range(n):
#         if check[i]:
#             continue
#         li.append(nums[i])
#         check[i] = 1
#         pick(order+1)
#         li.pop()
#         check[i] = 0


nums = [int(input()) for _ in range(9)]
nums.sort()
target_sum = sum(nums) - 100

for i in range(9):
    target_num = target_sum - nums[i]
    try:
        j = nums.index(target_num)
    except:
        continue
    else:
        # print answer
        for k in range(9):
            if k != j and k != i:
                print(nums[k])
        break
