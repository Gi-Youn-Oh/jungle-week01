def pick(order):
    if order == k:
        s.add(''.join(map(str, li)))
        return
    for i in range(n):
        if check[i]:
            continue
        li.append(nums[i])
        check[i] = 1
        pick(order+1)
        li.pop()
        check[i] = 0


n = int(input())
k = int(input())
nums = [int(input()) for _ in range(n)]
check = [0]*n
li, s = [], set()
pick(0)
print(len(s))
