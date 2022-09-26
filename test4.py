n = int(input())
num_list = []
for i in range(1,n+1):
    num_list.append(str(i))
    new_list =[]
    for i in range(len(num_list)):
        new_list.append(i)
        int(new_list[i])
print(new_list)        