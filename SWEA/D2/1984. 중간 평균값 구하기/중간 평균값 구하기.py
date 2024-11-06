T = int(input())

def sum_middle_number(T):
    for i in range(1, T+1):
        numbers = list(map(int, input().split()))
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))

        final = sum(numbers)
        print("#{} {}" .format(i, round(final / len(numbers))))

sum_middle_number(T)
