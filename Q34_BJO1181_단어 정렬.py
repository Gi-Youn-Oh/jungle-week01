from sys import stdin, stdout

how_many = int(stdin.readline())
words = [stdin.readline().strip() for _ in range(how_many)]

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    stdout.write(i + '\n')

# for i in words:
#     print(i)
# stdout.write(i + '\n')
