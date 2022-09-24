c = int(input())

for _ in range(c):
    n = int(input())
    for score in range(n):
        score = map(int, input().split())
        sum_score = sum(score)
        avg = sum_score/score
        if score > avg:


        
        print(f'{avg:.3f}%')

