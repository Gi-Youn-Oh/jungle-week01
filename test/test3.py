# sen = list(input())
# print(sen)

# # wkfjawifjlakwfd awklejflawkf
# # >['w', 'a', 'k', 'j', 'f', 'l'] 이런식

# sne = input().split()
# print(sne)

# # wkajflw wkajflewj
# # > ['wkfjlawjfk' 'wklajflw']

# wfjwkf = list()
# wfjwkf = list()
# wfjwkf = list()
# wfjwkf = list()
# wfjwkf = list()

# wfjwkf = int (wfjwkf)

# wfawgmklwajlkasjgdl

# 같은 단어 = ctrl + d 한개씩 추가 선택
# 쉬프트 방향기 > 한글자씩 추가 선택
# 쉬프트 + 컨트롤 > 한단어 선택 
# ctrl page up , down 창이동
# ctrl ~ 터미널 열기 커서이동
# ctrl b 탭창열고닫기


num_list = [ '561', '662', '444' , '784' ,'556' ,'645']

for i in num_list:
    sep = [i[0],i[1],i[2]]
    # i = '561'
    # > '5' '6' '1'
    for i in range(len(sep)):
        sep[i] = int(sep[i])

    # > 정수화

    if sep[0]-sep[1] == sep[1]-sep[2]:
        print("yes")
    else:
        print("no")

# 1. 한수 인지 아닌지 출력


# for i in range(len(num_list)):
#     num_list[i]=int(num_list[i])

# print(num_list)

# for i in range(len(num_list)):
#     num_list[i]=str(num_list[i])

# print(num_list)