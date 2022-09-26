from sys import stdin, stdout

N = int(stdin.readline())

check_list = [0] * (10001)

for i in range(N):
    input_num = int(stdin.readline())
    check_list[input_num] = check_list[input_num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            stdout.write(str(i) + '\n')
