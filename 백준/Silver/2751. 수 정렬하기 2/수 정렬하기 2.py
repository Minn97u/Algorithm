import sys

T = int(input())
li = list()

for i in range(T):
    li.append(int(sys.stdin.readline()))

li.sort(reverse=False)

for i in li:
    print(i)

# li.sort(key=lambda x: (x[1], x[0]))
