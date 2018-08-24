'''Implement TicTacToe'''
def check_lines(tac_):
    '''Checking rows and columns here'''
    line_1 = []
    line_2 = []
    for i in range(3):
        # for j in range(3):
        line_1.append(tac_[i].count('x'))
        line_2.append(tac_[i].count('o'))
    
    countlist_x = []
    countlist_y = []
    for i in range(3):
        count_x = 0
        count_y = 0
        for j in range(3):
            count_x += tac_[j][i].count('x')
            count_y += tac_[j][i].count('o')
        countlist_x.append(count_x)
        countlist_y.append(count_y)
    if 3 in line_1:
        return 'x'
    if 3 in line_2:
        return 'o'
    if 3 in countlist_x:
        return 'x'
    if 3 in countlist_y:
        return 'o'

def check_diagonal(toe_):
    ''' Checking diagonals here'''
    count_ = 0
    count_1 = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                # print(toe_[i][j])
                count_ += toe_[i][j].count('x')
                count_1 += toe_[i][j].count('o')
    # print(count_1)
    len_ = len(toe_[0])
    c_x = 0
    c_y = 0
    for i in range(len_-1, -1, -1):
        c_x += toe_[len_-1-i][i].count('x')
        c_y += toe_[len_-1-i][i].count('o')
    if count_1 == 3 or c_y == 3:
        return 'o'
    elif count_ == 3 or c_x == 3:
        return 'x'


def decide_winner(tic_):
    '''Deciding winner in this fucntion'''
    c_y = 0
    c_x = 0
    c_dot = 0
    for i in tic_:
        c_x += i.count('x')
        c_y += i.count('o')
        c_dot += i.count('.')
    if c_dot + c_x + c_y != 9:
        return "invalid input"
    if abs(c_x - c_y) != 1:
        return "invalid game"
    winner_ = check_lines(tic_)
    winner_1 = check_diagonal(tic_)
    if winner_:
        return winner_
    if winner_1:
        return winner_1
    return 'draw'

def main():
    '''This is main function'''
    tic_tac = []
    for i in range(3):
        tic_tac.append([])
        tic_tac[i] = input().split(' ')
    print(decide_winner(tic_tac))

if __name__ == '__main__':
    main()
