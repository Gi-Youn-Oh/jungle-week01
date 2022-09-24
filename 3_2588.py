# (1)
Num = input()
N1 = int(Num[0])*100 + int(Num[1])*10 + int(Num[2])

# (2)
Num = input()
N2 = int(Num[0])*100 + int(Num[1])*10 + int(Num[2])

# (3)
p_3 = (N2%10)*N1

# (4)
p_4 = ((N2%100)//10)*N1

# (5)
p_5 = (N2//100)*N1

# (6)
p_6 = p_3 + p_4*10 + p_5*100


print(p_3)
print(p_4)
print(p_5)
print(p_6)
