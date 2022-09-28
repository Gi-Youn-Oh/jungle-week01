from sys import stdin, stdout

# how_many = int(stdin.readline())
# words = [stdin.readline().strip() for _ in range(how_many)]
words = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
print('1', words)

# 중복 제거
words = list(set(words))
print('2', words)



# words.sort()
# print('3', words)
words.sort(key=len)
print('4', words)
