from operator import truediv


def decimal_check(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False

    for i in range(3, num-1, 2):
        if (num % i == 0):
            return False
    return True


how_many = int(input())

array_input = []
for i in range(how_many):
    array_input.append(int(input()))

for key in array_input:
    index1 = index2 = int(key/2)
    while True:
        if decimal_check(index2) and decimal_check(index1):
            print(index1, index2)
            break
        index1 -= 1
        index2 += 1
