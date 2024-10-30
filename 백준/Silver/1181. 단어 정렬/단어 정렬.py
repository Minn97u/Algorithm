import sys

T = int(input())
li = []

for i in range(T):
    word = sys.stdin.readline().strip('\n')
    li.append(word)

set_li = set(li)
li2 = list(set_li)
li2.sort(key= lambda x: (len(x),x))

for j in li2:
    print(j)
