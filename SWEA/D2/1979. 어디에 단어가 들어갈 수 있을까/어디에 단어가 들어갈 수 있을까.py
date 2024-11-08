T = int(input())

def find_puzzle(T):
    for ty in range(1, T+1):
        N, K = map(int, input().split())
        puzzle = [list(map(int, input().split())) for _ in range(N)]
        result = 0

        for i in range(N):
            sum = 0

            for j in range(N):
                if puzzle[i][j] == 1:
                    sum += 1
                if puzzle[i][j] == 0 or j == N-1:
                    if sum == K:
                        result += 1
                    sum = 0

            for j in range(N):
                if puzzle[j][i] == 1:
                    sum += 1
                if puzzle[j][i] == 0 or j == N-1:
                    if sum == K:
                        result += 1
                    sum = 0

        print("#{} {}".format(ty, result))

find_puzzle(T)