T = int(input())

def bus(T):
    for tc in range(1,T+1):
        N = int(input())
        bus_lst = []
        for _ in range(N):
            bus = list(map(int,input().split()))
            bus_lst.append(bus)

        P = int(input())
        bus_stop = [0]*P

        for i in range(P):
            S = int(input())
            for j in range(N):
                if bus_lst[j][0] <= S and bus_lst[j][1] >= S:
                    bus_stop[i] +=1

        print(f"#{tc}",*bus_stop)

bus(T)