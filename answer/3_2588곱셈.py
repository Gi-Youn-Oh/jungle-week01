inp1 = int(input())
inp2 = int(input())

out1 = inp1*((inp2%100)%10)
out2 = inp1*((inp2%100)//10)
out3 = inp1*(inp2//100)
res = inp1*inp2

print(out1, out2, out3, res, sep='\n')