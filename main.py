sudoku = [
    [0, 0, 0, 9, 0, 0, 0, 7, 1],
    [9, 0, 0, 0, 0, 3, 0, 5, 0],
    [0, 2, 5, 0, 4, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 1, 6, 0],
    [0, 4, 0, 8, 0, 1, 0, 0, 0],
    [0, 0, 6, 5, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 9, 2, 6, 0, 0],
    [2, 9, 8, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 9],
]


def print_sudoku(sudoku):
    """打印数独矩阵，格式化输出"""
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(sudoku[i][j], end=' ')
        print()


def is_valid(sudoku, row, col, num):
    """检查在指定位置放置数字是否有效"""
    # 检查行
    for x in range(9):
        if sudoku[row][x] == num:
            return False

    # 检查列
    for x in range(9):
        if sudoku[x][col] == num:
            return False

    # 检查3x3子网格
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False

    return True


def solve(sudoku):
    """使用回溯法求解数独"""
    # 找到一个空单元格
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                # 尝试填入1-9
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):
                        # 填入有效数字
                        sudoku[row][col] = num

                        # 递归求解剩余部分
                        if solve(sudoku):
                            return True

                        # 如果无解，回溯
                        sudoku[row][col] = 0

                # 尝试了所有数字都无效，表示当前路径无解
                return False

    # 所有单元格都已填满，找到解决方案
    return True

if solve(sudoku):
    print_sudoku(sudoku)
else:
    print('Failed to solve the sudoku')

