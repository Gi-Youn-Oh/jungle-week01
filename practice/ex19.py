abc, edf = input().split() #문자열로 두개 받음 [abc] [edf]

abc=int[::-1] # 문자열 abc 를 뒤집어서 정수화 [끝에서:시작점으로:역순]
edf=int[::-1] # step 의 수는 리스트의 순서 등차 

if abc > edf :
    print(abc)
else :
    print(edf)