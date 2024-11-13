T = int(input())

def box(T):
    for tc in range(1,T+1):
        N,Q = map(int, input().split())
        lst = [0]*N

        for tc2 in range(1,Q+1):
            L,R = map(int, input().split())

            for j in range(L-1,R):
                lst[j] = tc2
        print(f"#{tc}",*lst)


box(T)