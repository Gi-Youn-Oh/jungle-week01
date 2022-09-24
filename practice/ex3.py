from re import A


abc = int(input())
edf = int(input())
a = abc*((edf%100)%10) # 472*385에서 385의 1의자리만 남기려면 100으로나눈 나머지에 10으로나눈 나머지 = 일의자리 
b = abc*((edf%100)//10) # 마찬가지 10의자리는 100으로 나눈 나머지에서 10의자리로 나눈 몫
c = abc*(edf//100) 
# A=a*1
# B=b*10
# C=c*100
sum = abc*edf
print(a, b, c, sum, sep='\n') # sep='\n'줄바꿈