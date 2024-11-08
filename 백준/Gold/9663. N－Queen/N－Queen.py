def dfs(n):
    global answer
    if n == N:
        answer += 1
        return

    for j in range(N):
        if N1[j] == N2[n-j] == N3[n+j] == 0:
            N1[j] = N2[n-j] = N3[n+j] = 1
            dfs(n+1)
            N1[j] = N2[n-j] = N3[n+j] = 0


N = int(input())
answer = 0
N1 = [0] * N
N2 = [0] * (2*N)
N3 = [0] * (2*N)
dfs(0)
print(answer)