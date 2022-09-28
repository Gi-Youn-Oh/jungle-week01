from itertools import permutations
from sys import stdin


N = int(stdin.readline()[0])
nums = list(map(int, stdin.readline().split()))
operators = list(map(int,stdin.readline().split()))

per_operators = permutations()