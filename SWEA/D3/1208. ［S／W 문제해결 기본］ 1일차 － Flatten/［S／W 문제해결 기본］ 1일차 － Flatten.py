T = 10

for tc in range(1,T+1):
    dump = int(input())
    lst = list(map(int,input().split()))

    for _ in range(dump):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1

    lst.sort()
    ans = lst[-1] - lst[0]

    print(f"#{tc} {ans}")