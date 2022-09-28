import itertools
import time
time_now = time.time()
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nPr = itertools.permutations(arr, 10)
print("done")
print(time.time() - time_now)

# import time
# pos = [0] * 10
# flag = [False] * 10
# time_now = time.time()


# def set(i):
#     for j in range(10):
#         if not flag[j]:
#             pos[i] = j
#             if i == 9:
#                 pass
#             else:
#                 flag[j] = True
#                 set(i+1)
#                 flag[j] = False


# set(0)
# print("done")
# print(time.time() - time_now)
