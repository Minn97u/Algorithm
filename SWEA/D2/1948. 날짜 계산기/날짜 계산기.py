T = int(input())
day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for tc in range(1,T+1):
    A1,A2,B1,B2 = map(int,input().split())

    sum = 0
    for i in range(A1,B1+1):
        sum += day[i]

    sum1 = sum - (A2 + (day[B1]- B2)) + 1
    print(f"#{tc}",sum1)