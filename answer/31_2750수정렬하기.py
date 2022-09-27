x = int(input()) # N 개수 받기 
num_list = []  
for i in range(x):  # 수 넣는대로 리스트 만들기
    num_list.append(int(input()))
num_list1 = sorted(num_list)     # 정렬 후 반환
for i in range(len(num_list)): # 순서대로 출력 
    print(num_list1[i])



# 파이썬 리스트는 sort() 라는 메소드를 가지고 이 메소드는 리스트를 정렬된 상태로 변경한다. 또 sorted() 라는 내장 함수는 이터러블 객체로부터 정렬된 리스트를 생성한다.

# 파이썬에서 간단하게 정렬을 실행하려면 다음과 같이 sorted()를 호출하면 된다. sorted()는 기존의 리스트를 변경하는 것이 아니라 정렬된 새로운 리스트를 반환한다.

# >>> sorted([4, 2, 3, 5, 1])
# [1, 2, 3, 4, 5]
# 리스트의 메소드인 sort()를 사용하여도 정렬이 된다. 이 경우에는 리스트 자체를 변경해 버린다. 일반적으로 이것보다는 내장함수인 sorted()가 더 편리하다.

# >>> myList = [4, 2, 3, 5, 1]
# >>> myList.sort()
# >>> myList
# [1, 2, 3, 4, 5]
# 또한 sort()는 리스트만을 위한 메소드이지만 sorted() 함수는 어떤 이터러블 객체도 받을 수 있다. 예를 들어서 다음과 같은 딕셔너리 객체도 받을 수 있다.

# >>> sorted({3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'})
# [1, 2, 3, 4, 5]

# n.sort(reverse=True) 역순정렬