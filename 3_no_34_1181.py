import sys

def return_dic_ord_2str(str1,str2):
    # 사전순 첫번째 문자열 반환
    for i in range(len(str1)):
        if (ord(str1[i]) < ord(str2[i])):
            return str1
        else:
            return str2

N = int(sys.stdin.readline().split()[0])

strs = []
lens_num = [0]*50

for _ in range(N):
    str_in = sys.stdin.readline().split()[0]
    length = len(str_in)
    if str_in in strs:
        continue
    
    if len(strs) == 0:
        strs.append(str_in)
        continue

    cnt_under_length_str_num = 0
    cnt_andunder_length_str_num = 0
    for i in range(length):
        cnt_under_length_str_num += lens_num[i]
    for i in range(length+1):
        cnt_andunder_length_str_num += lens_num[i]
    
    for i in range(cnt_under_length_str_num,cnt_andunder_length_str_num+1):
        if strs[i] == return_dic_ord_2str(strs[i],str_in):
            continue
        else:
            strs.insert(i, str_in)
            break
    else:
        strs.insert(cnt_andunder_length_str_num,str_in)

    lens_num[length] += 1
for i in range(len(strs)):
    print(strs[i])

# 처음 짠 코드 - 시간 초과
# strs = []
# for _ in range(N):
#     str_in = sys.stdin.readline().split()[0]
#     for i in range(len(strs)):
#         if str_in in strs:
#             break
#         if len(strs[i]) == len(str_in):
#             if strs[i] == return_dic_ord_2str(str1=strs[i],str2=str_in):
#                 continue
#             else:
#                 strs.insert(i,str_in)
#                 break
#         elif len(strs[i]) > len(str_in):
#             strs.insert(i,str_in)
#             break
#     else:
#         strs.append(str_in)
# print(strs)
# for i in range(len(strs)):
#     print(strs[i])
