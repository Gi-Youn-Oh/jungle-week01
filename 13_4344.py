C = int(input())

for _ in range(C):
    nums = input().split()
    sum_score = 0
    N = int(nums[0])
    over_avg_cnt = 0
    for i in range(1, N+1):
        score = int(nums[i])
        sum_score += score
    
    avg_score = sum_score/N

    for i in range(1, N+1):
        score = int(nums[i])
        if score > avg_score:
            over_avg_cnt += 1
    over_avg_ratio = round((over_avg_cnt / N)*100, 3)

    print('%05.3f%%'%over_avg_ratio)