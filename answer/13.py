n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0] #평균구하기 (num[0]: 학생수 , nums[1:] 점수)
    cnt = 0 #평균이상 학생수
    for score in nums[1:]:
        if score>avg:
            cnt+=1 #평균이상 학생수 더하기
        rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')
#f-string 이외에도 2가지 방법 더있음
#python index [0:4] 해당 index 의 첫번째 부터 3번째까지
#index[0:]끝지점 지정안하면 끝까지 / index[:3] index의 [0]~[2]

