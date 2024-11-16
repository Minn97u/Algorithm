
T = int(input())

for tc in range(1,T+1):
    P,Q,R,S,W = map(int, input().split())
    fee = []

    fee.append(P*W)

    if W <= R:
        fee.append(Q)
    else:
        fee.append(Q+((W-R)*S))

    print(f"#{tc}",min(fee))
