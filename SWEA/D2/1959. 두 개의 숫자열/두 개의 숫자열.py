T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0

    if M>N:
        for i in range(M-N+1):
            sum = 0
            for j in range(N):
                sum += A[j] * B[j+i]
            if ans < sum:
                ans = sum
    else:
        for i in range(N-M+1):
            sum = 0
            for j in range(M):
                sum += B[j] * A[j+i]
            if ans < sum:
                ans = sum
    print(f"#{tc}",ans)