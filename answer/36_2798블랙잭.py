import sys   # 3개의 조합이 m 보다 작은 수를 새로운 리스트로 받는다 / 새로운 리스트 조합중에 최대 값을 출력한다.

input = sys.stdin.readline

n, m = map(int,input().split())

card = list(map(int,input().split()))

# print(card)

final_list = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] > m:
                continue
            else :
                answer = card[i]+card[j]+card[k]
                final_list.append(int(answer))
                
print(max(final_list))
