N = input()

def alphavet_to_number(N):
    num = [ord(char) - ord('A') + 1 for char in N]
    print(*num)

alphavet_to_number(N)