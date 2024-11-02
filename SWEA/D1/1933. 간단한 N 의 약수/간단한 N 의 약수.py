def game_1933(C):
    for i in range (1, C+ 1):
        if C % i == 0 :
            print(i, end=" ")

            
C = int(input())
game_1933(C)