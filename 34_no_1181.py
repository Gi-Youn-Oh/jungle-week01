import sys

def dic_1st_btwn2(str1, str2) -> bool:
    # 사전순 첫번째 문자열 반환
    for i in range(len(str1)):
        if (ord(str1[i]) < ord(str2[i])):
            return True
        elif(ord(str1[i]) == ord(str2[i])):
            continue
        else:
            return False

N = int(sys.stdin.readline().split()[0])

strs = []
lens = [0]*51

for _ in range(N):
    str_in = sys.stdin.readline().split()[0]
    len_in = len(str_in)

    # 중복 제거
    if str_in in strs:
        continue
    
    len_under = 0
    len_same = 0
    for i in range(len_in):
        len_under += lens[i]
    len_same = len_under + lens[len_in]

# len_in  3
# under   [1,2,3,4] > 4
# str len [1,1,2,2,3,3,3,3,4,4,5]
# str idx [0,1,2,3,4,5,6,7,8,9,10]
# same    [1,2,3,4,5,6,7,8] > 8
    for i in range(len_under, len_same):
        if not dic_1st_btwn2(strs[i], str_in):
            strs.insert(i, str_in)
            break
    else:
        strs.insert(len_same, str_in)
    # print(f'{len_under:2}{len_same:2} - {strs} ', end='')
    # i=0
    # lens[len_in] += 1
    # while True:
    #     print(f'{lens[i]:3}', end='')
    #     i += 1
    #     if i == N:
    #         break
    # print()


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
