from sys import stdin

N = int(stdin.readline())
li = list(map(int,stdin.readline().split()))

print(min(li), max(li))
