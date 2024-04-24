# N = int(input())


# def math_sign(t):
#     while(t):
#         sum = 0
#         for i in range (t):
#             a = int(input())
#             sum = sum + a
        
#         if (sum > 0):
#             print("+")
#         elif (sum < 0):
#             print("-")
#         else :
#             print("0")
        
# math_sign(N)
# 풀다가 해설을 보았다..


from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    li = [int(stdin.readline()) for i in range(N)]
    if sum(li) == 0:
        print("0")
    elif sum(li) > 0:
        print("+")
    else:
        print("-")