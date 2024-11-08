
def dfs(n,sum,cnt):
    global ans
    if n == N:
        if sum == S and cnt > 0:
            ans += 1
        return

    dfs(n+1,sum+lis[n],cnt+1)
    dfs(n+1,sum,cnt)

N,S = map(int,input().split())
lis = list(map(int,input().split()))
ans = 0
dfs(0,0,0)
print(ans)
