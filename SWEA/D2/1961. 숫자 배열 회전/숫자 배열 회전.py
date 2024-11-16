T = int(input())

def round_num(T):
    for tc in range(1,T+1):
        N = int(input())
        num = list(input().split() for _ in range(N))

        num_90 = [[0]*N for _ in range(N)]
        num_180 = [[0]*N for _ in range(N)]
        num_270 = [[0]*N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                num_90[i][j] = num[N-j-1][i]

        for i in range(N):
            for j in range(N):
                num_180[i][j] = num_90[N-j-1][i]

        for i in range(N):
            for j in range(N):
                num_270[i][j] = num_180[N-j-1][i]

        print('#{}'.format(tc))
        for i in range(N):
            for a in range(N):
                print(num_90[i][a], end='')
            print(end=' ')
            for b in range(N):
                print(num_180[i][b], end='')
            print(end=' ')
            for c in range(N):
                print(num_270[i][c], end='')
            print()


round_num(T)