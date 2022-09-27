def hanoi(n, start, destination, other) :
    if n==1:
        print(start, destination, sep= " ")
        return
    else:
        hanoi(n-1,start, destination, other)
        hanoi(1, start, other, destination)
        hanoi(n-1, other, destination, start)

n= int(input())
print(2**n-1)
if(n <=20):
    hanoi(n, 1, 2, 3)



