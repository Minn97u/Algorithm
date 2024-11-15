T = 10

def sumsum(T):
    for tc in range(1,T+1):
        S = int(input())
        lst = list(list(map(int,input().split())) for _ in range(100))
        ans = []
        suml = 0
        sumr = 0

        for i in range(100):
            sumi = 0
            sumj = 0
            for j in range(100):
                sumi += lst[i][j]
                sumj += lst[j][i]

                if i == j:
                    suml += lst[i][j]
                if i + j == 100:
                    sumr += lst[i][j]
            ans.append(sumi)
            ans.append(sumj)
        ans.append(suml)
        ans.append(sumr)

        print(f"#{tc}",max(ans))

sumsum(T)