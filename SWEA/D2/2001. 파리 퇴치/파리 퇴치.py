T = int(input())

def bug_attack(T):
    for ba in range(1,T+1):
        N, M = map(int, input().split())
        li = [list(map(int, input().split())) for _ in range(N)]

        max_v = 0
        for i in range(N-M+1):
            for j in range(N-M+1):
                sum = 0
                for x in range(i, i+M):
                    for y in range(j, j+M):
                        sum += li[x][y]
                if max_v < sum :
                    max_v = sum
        print(f"#{ba} {max_v}")


bug_attack(T)