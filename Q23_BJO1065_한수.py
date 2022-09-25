def hansu(num):
    answer = 99
    for i in range(100, num+1):
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            answer += 1

    return answer


def answer(num):
    if num < 100:
        return num

    elif num == 1000:
        return 144

    else:
        return hansu(num)


print(answer(int(input())))
