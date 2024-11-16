T = int(input())

for tc in range(1,T+1):
    lst = list(list(map(int, input().split())) for _ in range(9))
    result = 1

    for i in range(9):
        low_number = [1,2,3,4,5,6,7,8,9]
        col_number = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            if lst[i][j] in low_number:
                low_number.remove(lst[i][j])
            else:
                result = 0

        for j in range(9):
            if lst[j][i] in col_number:
                col_number.remove(lst[j][i])
            else:
                result = 0

    for j in range(0,9,3):
        for k in range(0,9,3):
            sqr_number = [1,2,3,4,5,6,7,8,9]
            for h in range(j,j+3):
                for i in range(k,k+3):
                    if lst[h][i] in sqr_number:
                        sqr_number.remove(lst[h][i])
                    else:
                        result = 0
    print(f"#{tc}",result)
