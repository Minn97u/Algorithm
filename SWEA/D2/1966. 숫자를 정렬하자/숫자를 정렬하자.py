T = int(input())

def line_number(T):
    for tc in range(1, T+1):
        N = int(input())

        numbers = list(map(int, input().split(" ")))
        numbers.sort(reverse= False)
        print(f"#{tc}", *numbers)

line_number(T)
