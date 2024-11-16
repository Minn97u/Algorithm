N = int(input())
numbers =list(range(1,N+1))
numbers1 = []

for num in numbers:
    num_str  = str(num)
    if '3' in num_str or '6' in num_str or '9' in num_str :
        app = num_str.count('3') + num_str.count('6')+ num_str.count('9')
        numbers1.append('-'*app)
    else:
        numbers1.append(num)

print(*numbers1)
