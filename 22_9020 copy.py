import sys

def is_prime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True

T = int(sys.stdin.readline().split()[0])

num_list = []
sorted_num_list = []

for _ in range(T):
    n = int(sys.stdin.readline().split()[0])
    num_list.append(n)
    sorted_num_list.append(n)
    ##############
sorted_num_list.sort
print(sorted_num_list)
print(num_list)



prime_list = [0]*10000
for num in range(2, 10000):
    if(is_prime(num)):
        prime_list[num]=num

    goldbach_list = [0,0]
    for num in range(n//2+1):
        if prime_list[num] != 0:
            if prime_list[num]+prime_list[n-num] == n:
                if goldbach_list[0] < num:
                    goldbach_list.remove(goldbach_list[0])
                    goldbach_list.remove(goldbach_list[0])
                    goldbach_list.append(num)
                    goldbach_list.append(n-num)
    print(goldbach_list[0],goldbach_list[1])