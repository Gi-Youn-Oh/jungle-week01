from sys import stdin

# disk      : 원판
# board     : 장대
def hanoi(disk, from_board,aux_board,to_board):
    # if disk <= 1:
        # print(f'{from_board} {to_board}')
    if disk >= 1:
        hanoi(disk-1, from_board, to_board, aux_board)
        print(f'{from_board} {to_board}')
        hanoi(disk-1, aux_board, from_board, to_board)

n = int(stdin.readline().split()[0])

print(2**n - 1)
if n <= 20:
    hanoi(n,1,2,3)


# if n < 20:
    
    
