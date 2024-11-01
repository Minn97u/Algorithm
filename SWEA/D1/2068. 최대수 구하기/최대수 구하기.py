T = int(input())

def find_max_number(T):
    for i in range(1, T+1):
        numbers = map(int, input().split())
        print(f"#{i} {max(numbers)}")

find_max_number(T)