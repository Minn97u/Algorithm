import sys

a = int(input())

b = list(map(int, sys.stdin.readline().split()))
    
c = int(input())

sum = 0

for i in range(a):
    if (b[i] == c):
        sum = sum + 1
        
print(sum)