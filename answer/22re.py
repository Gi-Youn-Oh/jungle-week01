# 시간 초과 다시풀기

T = int(input())

for _ in range(T):
    n = int(input())
    pull_list = list()
    for i in range(1, n+1):
        pull_list.append(i)

# print(pull_list)
    sosu_list = []
    for so in pull_list:
        for i in range(2, so):
            if so % i == 0:
                break
        else:
            if so == 1:
                pass
            else:
                sosu_list.append(so)

    for i in range(len(sosu_list)//2, -1,-1):
        if n - sosu_list[i] in sosu_list:
            if sosu_list[i] > n - sosu_list[i]:
                print(n-sosu_list[i], sosu_list[i])
            else:
                print(sosu_list[i],n-sosu_list[i])
            break
