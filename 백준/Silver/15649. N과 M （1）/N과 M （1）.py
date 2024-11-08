def dfs(n,lst):
    if n == M:
        answer.append(lst)
        return

    for j in range(1,N+1):
        if check[j] == 0:
            check[j] = 1
            dfs(n+1,lst+[j])
            check[j] = 0

N, M = map(int, input().split())

answer = []
check = [0] * (N+1)

dfs(0, [])
for lst in answer:
    print(*lst)