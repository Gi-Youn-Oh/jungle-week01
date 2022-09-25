def jaygui_start():
    print(A)
    what_is_jaygui(0)


def under_gen(i: int) -> None:
    return ("____" * i)


def what_is_jaygui(i):
    print(under_gen(i) + B)

    if i == jaygui_final:
        print(under_gen(i)+C_final)
    else:
        print(under_gen(i)+C1)
        print(under_gen(i)+C2)
        print(under_gen(i)+C3)

        what_is_jaygui(i+1)

    print(under_gen(i)+D)


A = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
B = '"재귀함수가 뭔가요?"'
C1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
C2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
C3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
C_final = '"재귀함수는 자기 자신을 호출하는 함수라네"'
D = '라고 답변하였지.'

jaygui_final = int(input())
jaygui_start()
