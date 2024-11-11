def dfs(n,sum,cnt):
    global ans
    if n == 12:
        if sum == K and cnt == N:
            ans += 1
        return

    dfs(n+1,sum+lst[n],cnt+1)
    dfs(n+1,sum,cnt)



T = int(input())
lst = [num for num in range(1, 13)]
for i in range(1, T+1):
    N,K = map(int, input().split())
    ans = 0
    dfs(0,0,0)
    print(f"#{i} {ans}")