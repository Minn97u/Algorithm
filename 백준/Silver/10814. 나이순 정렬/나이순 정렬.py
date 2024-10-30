import sys

T = int(input())
li = []

for i in range(T):
    age, word = sys.stdin.readline().strip('\n').split()
    age = int(age)
    li.append([age, word, i])


li.sort(key= lambda x: (x[0], x[2]))

for age, word, _ in li :
    print(age, word)