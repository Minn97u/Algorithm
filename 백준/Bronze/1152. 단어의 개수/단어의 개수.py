from sys import stdin

N = stdin.readline().rstrip()
li = list(N.split(" "))

li = list(filter(None, li))

print(len(li))
