import sys

# N - 주어지는 카드의 개수
# M - 고른 카드의 합의 최대값
N, M = list(map(int, sys.stdin.readline().split()))

cards = list(map(int, sys.stdin.readline().split()))

max_sum_cards = 0
# print(cards)

for idx in range(len(cards)):
    for jdx in range(idx + 1, len(cards)):
        for kdx in range(jdx + 1, len(cards)):
            pre_cards = cards[idx] + cards[jdx] + cards[kdx]

            if pre_cards > M:
                # print(f'{idx:3}{jdx:3}{kdx:3} -{max_sum_cards:4}- {pre_cards}')
                continue
            if pre_cards == M:
                max_sum_cards = pre_cards
                # print(idx,jdx,kdx)
                break

            if pre_cards > max_sum_cards:
                max_sum_cards = pre_cards
                # print(f'{idx:3}{jdx:3}{kdx:3} -{max_sum_cards:4}- {pre_cards}')
        if pre_cards == M:
            break
    if pre_cards == M:
            break
print(max_sum_cards)

# for idx, card_x in enumerate(cards):
#     for jdx, card_y in enumerate(cards, idx + 1):
#         for kdx, card_z in enumerate(cards, jdx + 1):
#             print(f'{idx:3}{jdx:3}{kdx:3}  -{card_x:3}{card_y:3}{card_z:3}')

# for idx, card_x in enumerate(cards):
#     for jdx, card_y in enumerate(cards, idx + 1):
#         for kdx, card_z in enumerate(cards, jdx + 1):
#             pre_sum_cards = card_x + card_y + card_z
#             if pre_sum_cards > M:
#                 continue
#             if pre_sum_cards == M:
#                 max_sum_cards = pre_sum_cards
#                 print(idx,jdx,kdx,card_x,card_y,card_z)
#                 break

#             if pre_sum_cards > max_sum_cards:
#                 max_sum_cards = pre_sum_cards
# print(max_sum_cards)