def count_bag(N):
    bag = 0
    while N >= 0:
        if N % 5 == 0:
            bag += (N // 5)
            print(bag)
            break
        N -= 3
        bag += 1
    else:
        print(-1)

N = int(input())
count_bag(N)