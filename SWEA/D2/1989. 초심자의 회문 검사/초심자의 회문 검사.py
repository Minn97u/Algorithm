N = int(input())

def sentence(N):
    for i in range(1, N+1):
        T = input()
        li = ''.join(T[::-1])

        if str(li) == T:
            print(f"#{i} 1")
        else:
            print(f"#{i} 0")

sentence(N)