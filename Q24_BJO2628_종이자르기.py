from array import array

x_end, y_end = map(int, input().split())

array_x = [0]
array_y = [0]
how_many = int(input())

for i in range(how_many):
    new_index, new_value = map(int, input().split())
    if new_index == 1:
        array_x.append(new_value)
    elif new_index == 0:
        array_y.append(new_value)
    else:
        print("SOEMTHING WRONG")

array_x.sort()
array_y.sort()
array_x.append(x_end)
array_y.append(y_end)

answer_x = []
answer_y = []
for i in range(len(array_x)-1):
    answer_x.append(array_x[i+1] - array_x[i])

for i in range(len(array_y)-1):
    answer_y.append(array_y[i+1] - array_y[i])

print(max(answer_x) * max(answer_y))
