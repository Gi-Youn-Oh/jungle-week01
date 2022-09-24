import sys

A, B, V = list(map(int, sys.stdin.readline().split()))

day = (V-A)//(A-B)
pre_height = day*(A-B)
# print(day,'-',pre_height)

while True:
    day += 1
    pre_height += A
    if pre_height >= V:
        break
    pre_height -= B

print(day)