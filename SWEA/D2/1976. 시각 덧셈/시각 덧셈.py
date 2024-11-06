T = int(input())

def plus_time(T):
    for i in range(1, T+1):
        H1,T1,H2,T2 = map(int,input().split(" "))
        hour, time = H1+H2,T1+T2

        if time > 60:
            hour += 1
            time -= 60
        if hour > 12:
            hour -= 12

        print("#{} {} {}" .format(i,hour,time))

plus_time(T)

