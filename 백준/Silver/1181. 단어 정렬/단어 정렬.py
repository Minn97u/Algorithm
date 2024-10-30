import sys

T = int(input())
li = []
value = []

for i in range(T):
    word = sys.stdin.readline().strip('\n')
    li.append(word)

li.sort(key= lambda x: (len(x),x))

for i in li:
    if i not in value:
        value.append(i)

for j in value:
    print(j)