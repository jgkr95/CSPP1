def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows_1 = len(m1_)
    columns_1 = len(m1_[0])
    rows_2 = len(m2_)
    columns_2 = len(m2_[0])
    multiply_both = []
    if columns_1 != rows_2:
        print("Error: Matrix shapes invalid for mult")
    else:
        for i in range(rows_1):
            multiply_both.append([])
            for j in range(columns_2):
                sum_ = 0
                for k in range(rows_2):
                    sum_ = sum_ + m1_[i][k] * m2_[k][j]
                multiply_both[i].append(sum_)
        # print(multiply_both)
    return multiply_both
def add_matrix(m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
        # if type(m1_) == None or type(m2_) == None:
        #     raise Exception
    rows_1 = len(m1_)
    columns_1 = len(m1_[0])
    rows_2 = len(m2_)
    columns_2 = len(m2_[0])
    add_both = []
    if rows_1 != rows_2 or columns_1 != columns_2:
        print("Error: Matrix shapes invalid for addition")
    else:
        for i in range(rows_1):
            add_both.append([])
            for j in range(columns_1):
                add_both[i].append(m1_[i][j]+m2_[i][j])
    # print(add_both)
    return add_both
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows_columns = input()
    rows_columns = rows_columns.split(',')
    rows_ = int(rows_columns[0])
    columns_ = int(rows_columns[1])
    # no_of_elements = 0
    total_ = 0
    # matrix1 = map(int, input().split(" "))
    mat = []
    for i in range(rows_):
        mat.append(input().split(" "))
        # print(mat)
        # print(len(mat[i]))
        total_ += len(mat[i])
    matrix = [list(map(int, i)) for i in mat]
    # for i in matrix:
    #   print(matrix[i])
        # no_of_elements += len(matrix[i])
    if total_ != rows_ * columns_:
        print("Error: Invalid input for the matrix")
        return 1, total_, rows_ * columns_

    return matrix, total_, rows_ * columns_
    # pass
def main():
    '''main function'''
    # read matrix 1
    # for iterate in range(2):
    # rows_columns = input()
    # rows_columns = rows_columns.split(',')
    # rows_ = int(rows_columns[0])
    # columns_ = int(rows_columns[1])
    # # matrix1 = map(int, input().split(" "))
    # mat = []
    # for i in range(rows_):
    #   mat.append(input().split(" "))
    # matrix1 = [list(map(int,  i)) for i in mat]
    # matrix1 = read_matrix()
    # print(matrix1)


    # read matrix 2
    # rows_columns2 = input()
    # rows_columns2 = rows_columns2.split(',')
    # rows_2 = int(rows_columns2[0])
    # columns_2 = int(rows_columns2[1])
    # # matrix1 = map(int, input().split(" "))
    # mat2 = []
    # for i in range(rows_):
    #   mat2.append(list(map(int, input().split(" "))))
    # print(mat2)
    # matrix2 = read_matrix()
    # print(matrix2)
    matrix_1 = list(read_matrix())
    matrix_2 = list(read_matrix())
    # print(matrix_1)
    # print(matrix_2[0])

    if matrix_1[0] != 1 and matrix_2[0] != 1:
        print(add_matrix(matrix_1[0], matrix_2[0]))

    # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_1[0], matrix_2[0]))

if __name__ == '__main__':
    main()
