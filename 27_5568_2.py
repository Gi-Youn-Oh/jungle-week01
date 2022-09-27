from itertools import permutations
from sys import stdin

n = int(stdin.readline().split()[0])
k = int(stdin.readline().split()[0])

cards = [stdin.readline().split()[0] for _ in range(n)]

picked_cards = set(permutations(cards, k))

no_repetition_num = set()

for card in picked_cards:
    num = ""
    for i in range(len(card)):
        num += card[i]
    num = int(num)
    no_repetition_num.add(num)
print(len(no_repetition_num))
