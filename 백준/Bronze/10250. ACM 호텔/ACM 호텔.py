T = int(input())

for i in range(T):
    a, b, c = map(int, input().split())
    floor = c % a
    num = c // a + 1
    if c % a == 0 :
        floor = a
        num = c // a
    print(f'{floor*100 + num}')