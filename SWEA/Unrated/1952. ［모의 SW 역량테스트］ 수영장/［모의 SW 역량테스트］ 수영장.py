def dfs(n,sum):
    global ans

    if n > 12:
        ans = min(ans,sum)
        return

    dfs(n+1,sum+(day*lst[n]))
    dfs(n+1,sum+mon)
    dfs(n+3,sum+mon3)
    dfs(n+12,sum+year)

T = int(input())

for i in range(1,T+1):
    day,mon,mon3,year = map(int,input().split())
    lst = [0] + list(map(int,input().split()))
    ans = 36000
    dfs(1,0)
    print(f"#{i} {ans}")