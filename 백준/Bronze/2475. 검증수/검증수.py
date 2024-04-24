import math

a, b, c, d, e  = map(int, input().split(" "))

def newcal(x, y, z, i, j):
    sum = int(math.pow(x,2) + math.pow(y,2) + math.pow(z,2) + math.pow(i,2) + math.pow(j,2))
    return print(sum % 10)
    
newcal(a, b, c, d, e)