'''Implement TicTacToe'''
def check_lines(tac_):
	line_1 = []
	line_2 = []
	for i in range(3):
		# for j in range(3):
		line_1.append(tac_[i].count('x'))
		line_2.append(tac_[i].count('o'))
	if 3 in line_1:
		return 'x'
	elif 3 in line_2:
		return 'o'
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
	if 3 in countlist_x:
		return 'x'
	elif 3 in countlist_y:
		return 'o'







			# if tac_[0][0] == tac_[0][1] == tac_[0][2]:
			# 	return 
def check_diagonal(toe_):
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
	for i in range(len_-1,-1,-1):
		c_x += toe_[len_-1-i][i].count('x')
		c_y += toe_[len_-1-i][i].count('o')
	if count_1 == 3 or c_y == 3:
		return 'o'
	elif count_ == 3 or c_x == 3:
		return 'x'


def decide_winner(tic_):
	# for i in tic_:
	# 	for j in 'xo.':
	# 		if j in i:
	# 			continue
	# 		else:
	# 			return "invalid input"
	c_y = 0
	c_x = 0
	for i in tic_:
		c_x += i.count('x')
		c_y += i.count('o')
	if abs(c_x - c_y) != 1:
		return "invalid game"
	w_ = check_lines(tic_)
	w_1 = check_diagonal(tic_)
	if w_:
		return w_
	if w_1:
		return w_1
	return 'draw'



def main():
	tic_tac = []
	for i in range(3):
		tic_tac.append([])
		tic_tac[i] = input().split(' ')
	print(decide_winner(tic_tac))

if __name__ == '__main__':
    main()
