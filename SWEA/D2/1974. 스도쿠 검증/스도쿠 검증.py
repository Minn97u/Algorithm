T = int(input())

def sudoku(T):
    for ty in range(1, T+1):
        num = [list(map(int, input().split())) for _ in range(9)]
        result = 1

        for i in range(9):
            row_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            col_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                if num[i][j] in row_check:
                    row_check.remove(num[i][j])
                else:
                    result = 0

                if num[j][i] in col_check:
                    col_check.remove(num[j][i])
                else:
                    result = 0

        for row in range(0,9,3):
            for col in range(0,9,3):
                square_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(3):
                    for j in range(3):
                        if num[row + i][col + j] in square_check:
                            square_check.remove(num[row + i][col + j])
                        else:
                            result = 0  # 중복되거나 잘못된 값이 있는 경우

        print("#{} {}".format(ty,result))

sudoku(T)