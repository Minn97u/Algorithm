T = int(input())
di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1, T+1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]
    i,j,cnt,dr = 0,0,1,0
    lst[i][j] = cnt
    cnt+=1

    while cnt <= N*N:
        ni = i + di[dr]
        nj = j + dj[dr]

        if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 0:
            i,j = ni,nj
            lst[i][j] = cnt
            cnt +=1
        else :
            dr = (dr+1) % 4

    print(f"#{tc}")
    for arr in lst:
        print(*arr)
