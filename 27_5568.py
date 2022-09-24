import sys

# def make_number(made_num_list, pre_num, num_list, i_list, k, start_num):
#     if len(i_list) == k:
#         if pre_num not in made_num_list:
#             made_num_list.append(pre_num)
#             pre_num = num_list[i_list[0]]
#             i_list.pop(1)
#         print(f'made_num_list-{made_num_list}, i_list-{i_list}, pre_num-{pre_num}')
#         # print(made_num_list)
#         return
#     for j in range(start_num, len(num_list)):
#         i_list = [j]
#         pre_num = num_list[j]
#         for i in range(len(num_list)):
#             if i in i_list:
#                 continue
#             i_list.append(i)
#             pre_num += num_list[i]
#             print(f'i-{i},j-{j} i_list-{i_list}, pre_num-{pre_num}, made_num_list-{made_num_list}')
#             make_number(made_num_list,pre_num,num_list,i_list,k,start_num+1)
#         # print()

# n = int(sys.stdin.readline().split()[0])
# k = int(sys.stdin.readline().split()[0])

# num_list = []
# made_num_list = []

# for _ in range(n):
#     num = sys.stdin.readline().split()[0]
#     num_list.append(num)

# pre_num = num_list[0]
# i_list = [0]

# make_number(made_num_list,pre_num,num_list,i_list,k,0)
# print(len(made_num_list))



# n = int(sys.stdin.readline().split()[0])
# k = int(sys.stdin.readline().split()[0])

# num_input_list = []
card_idx_list = []


# for _ in range(n):
#     num_input_list.append(sys.stdin.readline().split()[0])

def merge_k_num(idx,k):
    if k == 0:
        return
    
    if idx in card_idx_list:
        merge_k_num(idx + 1, k)
    else:
        card_idx_list.append(idx)
        merge_k_num(idx, k-1)

merge_k_num(0, 3)
print(card_idx_list)