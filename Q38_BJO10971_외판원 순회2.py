from sys import stdin, stdout

##initializing##
how_many = int(stdin.readline())
values = []
pos = [0] * how_many
flag = [False] * how_many

global min_val
min_val = 11000000

for i in range(how_many):
    value = list(map(int, stdin.readline().split()))
    values.append(value)


def set(i):
    global min_val
    for j in range(how_many):
        if not flag[j]:
            pos[i] = j
            if i == (how_many-1):
                result = calculate(pos, values, min_val)
                if result:
                    min_val = result
            else:
                flag[j] = True
                set(i+1)
                flag[j] = False


def calculate(index_arr, values, min_v):
    temp = []
    for i in index_arr:
        temp.append(i)
    temp.append(index_arr[0])  # back to the home
    costs = 0
    for i in range(len(temp)-1):
        cost = values[temp[i+1]][temp[i]]
        if cost == 0:
            return False

        costs += cost

        if costs > min_v:
            return False
    return costs

# run


set(0)
print(min_val)
