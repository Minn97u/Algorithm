N = int(input())

def game(N):
    numbers = list(range(1, N+1))
    numbers1 = ['-' * (str(num).count('3')+str(num).count('6')+str(num).count('9'))
               if '3' in str(num) or '6' in str(num) or '9' in str(num) else num for num in numbers]
    
    print(*numbers1, sep=' ') 

game(N)