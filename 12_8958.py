T = int(input())

for _ in range(T):
    ox_input = input()
    sum_ox = 0
    pre_score = 0
    for i in range(len(ox_input)):
        if(ox_input[i]=='O'):
            if(pre_score == 0):
                pre_score = 1
            elif(pre_score > 0):
                pre_score += 1
        else:
            pre_score = 0        
        sum_ox += pre_score
    print(sum_ox)
