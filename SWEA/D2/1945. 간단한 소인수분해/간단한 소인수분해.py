T = int(input())
number = [2,3,5,7,11]

for tc in range(1, T+1):
    N = int(input())
    check = [0]*5

    for i in range(5):
        while N % number[i] == 0:
            check[i] += 1
            N = N // number[i]

    print(f"#{tc}",*check)



