sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

sudoku_table = ""
row = 3
for i in sudoku:
    for k, char in enumerate(i):
        if row == 3:
            print(11 * '- ')
            row = 0
        sudoku_table += str(char) if k % 3 or k == 0 else '|' + str(char)
    row += 1
    print(*sudoku_table)
    sudoku_table = ""
print(11 * '- ')
