from asyncio.windows_events import NULL
import sys

N = int(sys.stdin.readline().split()[0])

nums = list(map(int,sys.stdin.readline().split()))
ordered_nums = []

# 넣으면서 크기순으로 정렬? > 안됨. 문제 조건이 그렇게 못하게 해놓음 > 따로 정렬하는 파트 만들어야됨.

# 크기순 정렬
for i in range(N):
    num = nums[i]
    for j in range(len(ordered_nums)):
        if num < ordered_nums[j]:
            ordered_nums.insert(j, num)
            # ordered_nums.insert(j+1, 0)
            break
    else:
        ordered_nums.append(num)
        # ordered_nums.append(0)
# print(ordered_nums)
# 0인 값들을 바꿔주기
# for i in range(N):
#     back_idx = -i-1
#     if ordered_nums[i] == 0:
#         ordered_nums[i] = ordered_nums[back_idx]
#         # print(back_idx, ordered_nums[i],ordered_nums[back_idx])
# print(ordered_nums)



# 3개일때는 다르게 짜야됨.
print(ordered_nums)
if len(ordered_nums) == 3:
    print(ordered_nums[2] * 2 - ordered_nums[1] - ordered_nums[0])
else:
    # 전체 개수가 4개 이상일 때
    # 앞 뒤에서 하나씩 꺼내서 넣는다.
    linked_li = [ordered_nums[-2], ordered_nums[0], ordered_nums[-1]]

    prev = 0
    last_idx = 2 # last_idx 인덱스는 계속 갱신이 필요함.
    max_sum = abs(linked_li[0] - linked_li[1]) + abs(linked_li[1] - linked_li[2])

    print(max_sum, linked_li)
    if len(ordered_nums) % 2 == 0:
        for n in range(1, len(ordered_nums) // 2):
            prev_dif = abs(linked_li[0] - ordered_nums[n])
            last_dif = abs(linked_li[last_idx] - ordered_nums[n])

            print(ordered_nums[n], prev_dif, last_dif, end = ' ')
            if prev_dif > last_dif:
                linked_li.insert(0,ordered_nums[n])
                max_sum += prev_dif
                print("prev")
            else:
                linked_li.append(ordered_nums[n])
                max_sum += last_dif
                print("last")
            # 만약에 차이의 절댓값이 같은 경우에는 이 방식이 안될수도?
            # >> 같을 수가 없음. 같을려면 똑같은 수가 3개 들어와야됨.
            # >>>> 같은 수(3)가 2번 들어오게 되면 이렇게 됨 - [3, ... , 3]
            # >>>>>> 만약 여기서 3이 한번더 들어오면 어디 붙이든지 간에 상관없음 그러므로 같은 경우는 크게 신경 안써도 됨.


            last_idx += 1 # last_idx 인덱스 갱신
    else:
        for n in range(1, len(ordered_nums) // 2 + 1):
            prev_dif = abs(linked_li[0] - ordered_nums[n])
            last_dif = abs(linked_li[last_idx] - ordered_nums[n])

            print(ordered_nums[n], prev_dif, last_dif, end = ' ')
            if prev_dif > last_dif:
                linked_li.insert(0,ordered_nums[n])
                max_sum += prev_dif
                print("prev")
            else:
                linked_li.append(ordered_nums[n])
                max_sum += last_dif
                print("last")
            # 만약에 차이의 절댓값이 같은 경우에는 이 방식이 안될수도?
            # >> 같을 수가 없음. 같을려면 똑같은 수가 3개 들어와야됨.
            # >>>> 같은 수(3)가 2번 들어오게 되면 이렇게 됨 - [3, ... , 3]
            # >>>>>> 만약 여기서 3이 한번더 들어오면 어디 붙이든지 간에 상관없음 그러므로 값이 같은 경우는 이미 포함이 됨.

            last_idx += 1 # last_idx 인덱스 갱신

    print(max_sum, linked_li)
