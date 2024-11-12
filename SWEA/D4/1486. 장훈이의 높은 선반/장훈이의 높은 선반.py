def dfs(n, sum):
    global ans

    if n == N:
        if sum >= B:
            ans = min(ans,sum-B)
        return

    dfs(n+1, sum+lst[n])
    dfs(n+1, sum)


T = int(input())

for i in range(1,T+1):
    N,B = map(int, input().split())
    lst = list(map(int,input().split()))
    ans = N*10000

    dfs(0,0)
    print(f"#{i} {ans}")