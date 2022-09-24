import sys

a,b = sys.stdin.readline().split()


A = int(a[0])+int(a[1])*10+int(a[2])*100
B = int(b[0])+int(b[1])*10+int(b[2])*100
print(max(A, B))
