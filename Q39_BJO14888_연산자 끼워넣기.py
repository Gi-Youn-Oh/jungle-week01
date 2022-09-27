from glob import glob
from sys import stdin, stdout


def calculator(a, b, index):
    if index == 1:
        return a+b
    elif index == 2:
        return a-b
    elif index == 3:
        return a*b
    elif index == 4:
        if a*b < 0:
            return (abs(a) // abs(b) * (-1))
        else:
            return a//b
    else:
        print("!!!something WRONG!!!")
        return


def calculate_all(ordered_list: list, debug=False) -> int:
    result = input_nums[0]
    for i in range(len(ordered_list)):
        result = calculator(result, input_nums[i+1], ordered_list[i])
    return result


def set_op(i):
    global min_val
    global max_val

    for j in range(how_many-1):
        if not flag[j]:
            pos[i] = input_operators[j]
            if i == (how_many - 2):

                final_result = calculate_all(pos)
                if final_result < min_val:
                    min_val = final_result
                if final_result > max_val:
                    max_val = final_result
            else:
                flag[j] = True
                set_op(i+1)
                flag[j] = False


def operator_gen(arr: list) -> list:
    operators = []
    for i in range(len(arr)):
        if arr[i]:
            operators += [i+1] * arr[i]
    # 1 = +, 2 = -, 3 = X, 4 = //
    return operators


how_many = int(stdin.readline())
input_nums = list(map(int, stdin.readline().split()))
input_operators = value = list(map(int, stdin.readline().split()))
input_operators = operator_gen(input_operators)
flag = [False] * len(input_operators)
pos = [0] * len(input_operators)

global min_val
min_val = 1000000000

global max_val
max_val = -1000000000

# run
set_op(0)
print(max_val)
print(min_val)
