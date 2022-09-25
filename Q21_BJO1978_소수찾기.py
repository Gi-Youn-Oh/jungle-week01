//1978소수찾기
list_len = input()
array_input = list(map(int, input().split()))
max_num = max(array_input)

decimal_list = list(range(3, max_num+1, 2))
list_len = len(decimal_list)
check_list = [0]*list_len

# 최대값 미만의 소수 찾기
# ... 0~max_num까지의 소수찾기 알고리즘 가동
#decimal_list = [3,5,7,9,11,13,15,17]
#check_list =   [0,0,0,0, 0, 0, 0, 0]
for i in range(list_len):
    checker = decimal_list[i]
    for j in range(i, list_len):
        if i == j:
            continue
        # 아직 체크표시가 안되었다?? 소수인지 아닌지 모른다면?
        elif check_list[j] == 0:
            # 한번 나눠 봐야지!
            if decimal_list[j] % checker == 0:
                check_list[j] = 1
# 소수 array done

# Let's run
list_len = 0
if 2 in array_input:
    list_len += 1

for i in array_input:
    if i in decimal_list:
        if check_list[decimal_list.index(i)] == 0:
            list_len += 1

print(list_len)
