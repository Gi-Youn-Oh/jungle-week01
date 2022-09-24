import sys

X, Y = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline().split()[0])

cut_width = 1
cut_height = 1
cut_width_list = [0, X]
cut_height_list = [0, Y]


for _ in range(N):
    x_or_y, line_num = list(map(int, sys.stdin.readline().split()))
    if x_or_y == 1:
        cut_width += 1
        cut_width_list.append(line_num)
    elif x_or_y == 0:
        cut_height += 1
        cut_height_list.append(line_num)

num_of_square = cut_height * cut_width

cut_height_list.sort()
cut_width_list.sort()
max_width = 0
max_height = 0
for i in range(1,len(cut_width_list)):
    pre_width = cut_width_list[i]-cut_width_list[i-1]
    if max_width < pre_width:
        max_width = pre_width
for i in range(1,len(cut_height_list)):
    pre_height = cut_height_list[i]-cut_height_list[i-1]
    if max_height < pre_height:
        max_height = pre_height
print(max_height*max_width)

