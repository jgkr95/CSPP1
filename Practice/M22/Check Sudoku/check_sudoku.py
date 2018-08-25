'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
# def check_grid(grid):
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # print(sudoku)
    for row in sudoku:
        if sum(row) != 45:
            return False
    for i in range(9):
        sum_of_column = 0
        for j in range(9):
            sum_of_column += sudoku[j][i]
        if sum_of_column != 45:
            return False
    sum_grids = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 3):
        for j in sudoku[i][0:3]:
            sum_grids[0] += j
        # print(sudoku[i][0:3])
        for k in  sudoku[i][3:6]:
            sum_grids[1] += k
        # print(sudoku[i][3:6])
        for l_l in sudoku[i][6:9]:
            sum_grids[2] += l_l
        # print(sudoku[i][6:9])
    for i in range(3, 6):
        for j in sudoku[i][0:3]:
            sum_grids[3] += j
        # print(sudoku[i][0:3])
        for k in sudoku[i][3:6]:
            sum_grids[4] += k
        for l_l in sudoku[i][6:9]:
            sum_grids[5] += l_l
    for i in range(6, 9):
        for j in sudoku[i][0:3]:
            sum_grids[6] += j
        for k in sudoku[i][3:6]:
            sum_grids[7] += k
        for l_l in sudoku[i][6:9]:
            sum_grids[8] += l_l
    if sum(sum_grids) == 405:
        return True
    return None

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    sudoku = [list(map(int, i)) for i in sudoku]
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
