import time

class Board:
	current_state = ''
	A = 1
	B = 2
	C = 3
	D = 4
	E = 5
	F = 6
	G = 7
	H = 8

	HORIZONTAL = 1
	VERTICAL = 2

	OPPONENT_CHAR = 'O'
	COMPUTER_CHAR = 'X'
	EMPTY_CHAR = '-'
	WALL = 'W'

	HORIZONTAL = 0
	VERTICAL = 1

	COMPUTER = 0
	OPPONENT = 1

	MAX_DEPTH = 5

	number_of_empty_cells = 64
	
	def __init__(self):
		self.current_state = [[' ', 1, 2, 3, 4, 5, 6, 7, 8]]
		self.current_state.append(['A', '-', '-', '-', '-', '-', '-', '-', '-', ])
		self.current_state.append(['B', '-', '-', '-', '-', '-', '-', '-', '-', ])
		self.current_state.append(['C', '-', '-', '-', '-', '-', '-', '-', '-', ])
		self.current_state.append(['D', '-', '-', '-', '-', '-', '-', '-', '-', ])
		self.current_state.append(['E', '-', '-', '-', '-', '-', '-', '-', '-', ])
		self.current_state.append(['F', '-', '-', '-', '-', '-', '-', '-', '-', ])
		self.current_state.append(['G', '-', '-', '-', '-', '-', '-', '-', '-', ])
		self.current_state.append(['H', '-', '-', '-', '-', '-', '-', '-', '-', ])

		# if number_of_empty_cells == 0, then we have reached a terminal state
		self.number_of_empty_cells = 64

	def print_board(self):
		for row in range(0, 9):
			for col in range(0, 9):
				print(self.current_state[row][col], end = ' ')
			print()

	def get_number_of_empty_cells(self):
		return self.number_of_empty_cells

	def decrement_number_of_empty_cells(self):
		self.number_of_empty_cells -= 1

	def is_terminal(self):
		if self.get_number_of_empty_cells() == 0:
			return True
		else:
			return False

	def get_a_move(self):
		# check if the move is legal
		print('Make a move: ')
		move = input('')
		
		while self.check_move(move) == False:
			print('Please make a move again')
			move = input('')

	
		row = move[:1]
		col = move[1:]

		row = row.upper()
		col = int(col)

		self.place_the_move(row, col, self.OPPONENT_CHAR)

		

	def check_move(self, move):
		# check the length of the entered string
		# if > 2, then invalid, if < 2, then invalid
		

		if len(move) != 2:
			print('Invalid Move.')
			return False
		elif (move[:1] >= 'A' and move[:1] <= 'H') or (move[:1] >= 'a' and move[:1] <= 'h'):
			if (int(move[1:]) >= 1 and int(move[1:]) <= 8):
				
				row = move[:1]
				col = int(move[1:])

				row = ord(row.upper()) - 64

				if self.current_state[row][col] == self.EMPTY_CHAR:
					return True
				else:
					print('Invalid Move. The cell is already occupied.')
					return False
		else:
			print('Invalid Move.')
			return False 

	# given the move (row and col), it places the character (either 'X' for computer or 
	#	'O' for the user) to the specified location
	def place_the_move(self, row, col, char_to_place):
		if row == 'A':
			row = self.A
		elif row == 'B':
			row = self.B
		elif row == 'C':
			row = self.C
		elif row == 'D':
			row = self.D
		elif row == 'E':
			#print('herre')
			row = self.E
		elif row == 'F':
			row = self.F
		elif row == 'G':
			row = self.G
		elif row == 'H':
			row = self.H

		# !!! if the opponent (user) is doing the move, place 'O', otherwise, place 'X'
		if char_to_place == self.COMPUTER_CHAR:
			self.current_state[row][col] = self.COMPUTER_CHAR
		else:
			self.current_state[row][col] = self.OPPONENT_CHAR
		#self.decrement_number_of_empty_cells()

		return [row, col]

	#def horizontal_test(self, char_to_check, new_move_row, new_move_col):
	def horizontal_test(self, char_to_check):
		# test the player
		# the number of same characters in a row
		sequence_length = 0
		sequence_started = False
		if char_to_check == self.OPPONENT_CHAR:
			value_to_return = -50000
		else:
			value_to_return = 50000

		for row in range(1, 9):
			for col in range(1, 9):
		
			# if the cell has the player's/computer's character, depending on the value of
			#	char_to_check
				if self.current_state[row][col] == char_to_check:
					sequence_started = True
					sequence_length += 1
					if sequence_length == 4:
						return value_to_return
				# if the cell does not have the player's character, then stop counting this
				#	sequence, and reset the sequence_length back to 0
				else:
					sequence_started = False
					sequence_length = 0

			sequence_started = False
			sequence_length = 0

		# set sequence_length back to 0, and sequence_started to false as the row ended
		sequence_started = False
		sequence_length = 0

		# if no winning move has been found, return 1 (for a draw)
		value_to_return = 0
		return value_to_return

	#	exact repetition of horizontal_test, with the order of the two nested loops flipped
	#def vertical_test(self, char_to_check, new_move_row, new_move_col):
	def vertical_test(self, char_to_check):
		sequence_length = 0
		sequence_started = False

		if char_to_check == self.OPPONENT_CHAR:
			value_to_return = -50000
		else:
			value_to_return = 50000


		for col in range(1, 9):
			for row in range(1, 9):


				if self.current_state[row][col] == char_to_check:
					sequence_started = True
					sequence_length += 1
					if sequence_length == 4:
						#print('row = ' + row)
						#print('col = ' + col)
						return value_to_return
				else:
					sequence_started = False
					sequence_length = 0

			sequence_started = False
			sequence_length = 0

		sequence_started = False
		sequence_length = 0

		value_to_return = 0
		return value_to_return


	def evaluate_2(self, char_to_check):

		if char_to_check == self.COMPUTER_CHAR:
			other_char = self.OPPONENT_CHAR
			SIGN = 1
		else:
			other_char = self.COMPUTER_CHAR
			SIGN = -1

		difference = 0

		num_of_char_to_check = 0
		num_of_other_char = 0

		for row in range(1, 9):
			for col in range(1, 9):
				current_cell = self.current_state[row][col]

				if current_cell == char_to_check:
					num_of_char_to_check += 1
				elif current_cell == other_char:
					num_of_other_char += 1

			difference += num_of_char_to_check - num_of_other_char
			# reset the number of char_to_check and num_of_other_char
			num_of_char_to_check = 0
			num_of_other_char = 0

		if difference < 0:
			difference = difference * (-1)
			SIGN = SIGN * (-1)
	
		value_to_return = pow(5, difference)


		return value_to_return * SIGN

	# returns 
	#def evaluate(self, char_to_check, new_move_row, new_move_col):
	def evaluate(self, char_to_check):
		# evaluate horizontally
		current_value = 0
		best_value_so_far = 0

		previous_cell = ''
		current_cell = ''
		next_cell = ''

		# if the next_cell is a wall, then check the previous_previous_cell
		# if the previous_cell is a wall, then check the next_next_cell
		previous_previous_cell = 0
		next_next_cell = 0


		if char_to_check == self.COMPUTER_CHAR:
			other_char = self.OPPONENT_CHAR
		else:
			other_char = self.COMPUTER_CHAR


		case_1_2_x = 0
		case_3_4_x = 0
		case_5_x = 0
		case_6_7_x = 0

		case_1_2_o = 0
		case_3_4_o = 0
		case_5_o = 0
		case_6_7_o = 0

		for row in range(1, 9):
			for col in range(1, 9):
				if col > 1:
					previous_cell = self.current_state[row][col - 1]
				else:
					# else, the previous cell is a wall
					previous_cell = self.WALL


				current_cell = self.current_state[row][col]
				
				orientation = self.HORIZONTAL

				if char_to_check == self.COMPUTER_CHAR:
					case_1_2_x += self.check_case_1_2(char_to_check, row, col, orientation)
					case_3_4_x += self.check_case_3_4(char_to_check, row, col, orientation)
					case_5_x += self.check_case_5(char_to_check, row, col, orientation)
					case_6_7_x += self.check_case_6_7(char_to_check, row, col, orientation)

					case_1_2_o += self.check_case_1_2(other_char, row, col, orientation)
					case_3_4_o += self.check_case_3_4(other_char, row, col, orientation)
					case_5_o += self.check_case_5(other_char, row, col, orientation)
					case_6_7_o += self.check_case_6_7(other_char, row, col, orientation)

					orientation = self.VERTICAL
					case_1_2_x += self.check_case_1_2(char_to_check, row, col, orientation)
					case_3_4_x += self.check_case_3_4(char_to_check, row, col, orientation)
					case_5_x += self.check_case_5(char_to_check, row, col, orientation)
					case_6_7_x += self.check_case_6_7(char_to_check, row, col, orientation)

					case_1_2_o += self.check_case_1_2(other_char, row, col, orientation)
					case_3_4_o += self.check_case_3_4(other_char, row, col, orientation)
					case_5_o += self.check_case_5(other_char, row, col, orientation)
					case_6_7_o += self.check_case_6_7(other_char, row, col, orientation)
				else:
					case_1_2_x += self.check_case_1_2(other_char, row, col, orientation)
					case_3_4_x += self.check_case_3_4(other_char, row, col, orientation)
					case_5_x += self.check_case_5(other_char, row, col, orientation)
					case_6_7_x += self.check_case_6_7(other_char, row, col, orientation)

					case_1_2_o += self.check_case_1_2(char_to_check, row, col, orientation)
					case_3_4_o += self.check_case_3_4(char_to_check, row, col, orientation)
					case_5_o += self.check_case_5(char_to_check, row, col, orientation)
					case_6_7_o += self.check_case_6_7(char_to_check, row, col, orientation)

					orientation = self.VERTICAL
					case_1_2_x += self.check_case_1_2(other_char, row, col, orientation)
					case_3_4_x += self.check_case_3_4(other_char, row, col, orientation)
					case_5_x += self.check_case_5(other_char, row, col, orientation)
					case_6_7_x += self.check_case_6_7(other_char, row, col, orientation)

					case_1_2_o += self.check_case_1_2(char_to_check, row, col, orientation)
					case_3_4_o += self.check_case_3_4(char_to_check, row, col, orientation)
					case_5_o += self.check_case_5(char_to_check, row, col, orientation)
					case_6_7_o += self.check_case_6_7(char_to_check, row, col, orientation)
 

		return case_1_2_x + case_3_4_x + case_5_x + case_6_7_x + case_1_2_o + case_3_4_o + case_5_o + case_6_7_o



	def undo_move(self, row, col):
		self.current_state[row][col] = self.EMPTY_CHAR

	# returns 50 if case 1 holds, returns 0 if it does not hold
	#1)	| O - or - O | or .. X O - .. or .. - O X .. - 50
	#	4 possible arrangements
	#	| O -
	#	X O -
	#   - O |
	#	- O X
	#2) .. - O - ... - 100
	#   1 possible arrangement
	#	- O -
	def check_case_1_2(self, char_to_check, row, col, orientation):
		



		current_cell = self.current_state[row][col] 
		previous_cell = ''
		next_cell = ''



		if char_to_check == self.OPPONENT_CHAR:
			other_char = self.COMPUTER_CHAR
			SIGN = -1
		else:
			other_char = self.OPPONENT_CHAR
			SIGN = 1

		# if the current_cell is not char_to_check, return 0
		if current_cell != char_to_check:
			return 0
		else:
			if orientation == self.HORIZONTAL:
				if col == 1:
					previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row][col - 1]

				if col == 8:
					next_cell = self.WALL
				else:
					next_cell = self.current_state[row][col + 1]
			# orientation is VERTICAL
			# swap the col with row in all the occurances, and increment/decrement row 
			#	instead of col
			else:
				if row == 1:
					previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row - 1][col]

				if row == 8:
					next_cell == self.WALL
				else:
					next_cell = self.current_state[row + 1][col]




			#	| O -
			if previous_cell == self.WALL and next_cell == self.EMPTY_CHAR:
				return 50 * SIGN
			#	X O -
			elif previous_cell == other_char and next_cell == self.EMPTY_CHAR:
				return 50 * SIGN
			#   - O |
			elif previous_cell == self.EMPTY_CHAR and next_cell == self.WALL:
				return 50 * SIGN
			#	- O X
			elif previous_cell == self.EMPTY_CHAR and next_cell == other_char:
				return 50 * SIGN
			# check if case 2 holds
			# - O -
			elif previous_cell == self.EMPTY_CHAR and next_cell == self.EMPTY_CHAR:
				return 100 * SIGN
			else:
				return 0

	#3) | O O - or - O O | or .. X O O - or - O O X .. - 200
	# 	4 possible arrangements
	#	| O O -
	#	X O O -
	#	- O O |
	#	- O O X
	#	Other 4 possible arrangements, with O substituted with X and X substituted with O
	#	char_to_ckeck takes care of the cases
	#4)	.. - O O - ... - 1000
	def check_case_3_4(self, char_to_check, row, col, orientation):
		current_cell = self.current_state[row][col]
		previous_cell = ''

		next_cell = ''
		next_next_cell = ''

		if char_to_check == self.OPPONENT_CHAR:
			other_char = self.COMPUTER_CHAR
			SIGN = -1
		else:
			other_char = self.OPPONENT_CHAR
			SIGN = 1

		if current_cell != char_to_check:
			return 0
		else:
			if orientation == self.HORIZONTAL:
				if col == 1:
					previous_cell = self.WALL
					previous_previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row][col - 1]
				
				if col == 8:
					next_cell = self.WALL
				else:
					next_cell = self.current_state[row][col + 1]
					if col < 7:
						next_next_cell = self.current_state[row][col + 2]
					else:
						next_next_cell = self.WALL
			# orientation is VERTICAL
			else:
				if row == 1:
					previous_cell = self.WALL
					previous_previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row - 1][col]
				
				if row == 8:
					next_cell = self.WALL
				else:
					next_cell = self.current_state[row + 1][col]
					if row < 7:
						next_next_cell = self.current_state[row + 2][col]
					else:
						next_next_cell = self.WALL

			# check this:	| O O -, current_cell is the 1st O to the right of the wall
			if previous_cell == self.WALL and next_cell == char_to_check and next_next_cell == self.EMPTY_CHAR:
				return 200 * SIGN
			# X O O -    current_cell is the 1st O after X
			elif previous_cell == other_char and next_cell == char_to_check and next_next_cell == self.EMPTY_CHAR:
				return 200 * SIGN
			#	- O O | current_cell is the 1st O after -
			elif previous_cell == self.EMPTY_CHAR and next_cell == char_to_check and next_next_cell == self.WALL:
				return 200 * SIGN
			#	- O O X current_cell is the 1st O after -
			elif previous_cell == self.EMPTY_CHAR and next_cell == char_to_check and next_next_cell == other_char:
				return 200 * SIGN
			# - O O - current_cell is the 1st O after -
			elif previous_cell == self.EMPTY_CHAR and next_cell == char_to_check and next_next_cell == self.EMPTY_CHAR:
				return 2000 * SIGN
			# # - O O - current_cell is the 2nd O after - 
			# elif previous_cell == char_to_check and previous_previous_cell == self.EMPTY_CHAR and next_cell == self.EMPTY_CHAR:
			# 	return 400	
			else:
				return 0
			
	#5) .. O - O O .. or .. O O - O - 20000
	# .. O - O O .. 
	# .. O O - O ..
	def check_case_5(self, char_to_check, row, col, orientation):
		current_cell = self.current_state[row][col]
		previous_cell = ''
		previous_previous_cell = ''
		next_cell = ''
		next_next_cell = ''


		if char_to_check == self.OPPONENT_CHAR:
			other_char = self.COMPUTER_CHAR
			SIGN = -1
		else:
			other_char = self.OPPONENT_CHAR
			SIGN = 1

		if current_cell != self.EMPTY_CHAR:
			return 0
		else:
			if orientation == self.HORIZONTAL:
				if col == 1:
					previous_cell = self.WALL
					previous_previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row][col - 1]
					if col > 2:
						previous_previous_cell = self.current_state[row][col - 2]

				if col == 8:
					next_cell = self.WALL
				else:
					next_cell = self.current_state[row][col + 1]
					if col < 7:
						next_next_cell = self.current_state[row][col + 2]
					else:
						next_next_cell = self.WALL
			# orientation is VERTICAL
			else:
				if row == 1:
					previous_cell = self.WALL
					previous_previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row - 1][col]
					if row > 2:
						previous_previous_cell = self.current_state[row - 2][col]

				if row == 8:
					next_cell = self.WALL
				else:
					next_cell = self.current_state[row + 1][col]
					if row < 7:
						next_next_cell = self.current_state[row + 2][col]
					else:
						next_next_cell = self.WALL


			# .. O - O O .. current_cell is the '-'
			if previous_cell == char_to_check and next_cell == char_to_check and next_next_cell == char_to_check:
				return 20000 * SIGN
			# .. O O - O .. current_cell is the '-'
			elif previous_cell == char_to_check and previous_previous_cell == char_to_check and next_cell == char_to_check:
				return 20000 * SIGN
			else:
				return 0

	#6)	| O O O - or - O O O | or .. X O O O - or - O O O X .. 5000
	# | O O O -
	# - O O O |
	# X O O O -
	# - O O O X
	#7)	.. - O O O - ... - 10000
	def check_case_6_7(self, char_to_check, row, col, orientation):
		current_cell = self.current_state[row][col]
		previous_cell = ''
		#previous_previous_cell = ''
		next_cell = ''
		next_next_cell = ''
		next_next_next_cell = ''

		if char_to_check == self.OPPONENT_CHAR:
			other_char = self.COMPUTER_CHAR
			SIGN = -1
		else:
			other_char = self.OPPONENT_CHAR
			SIGN = 1

		if current_cell != char_to_check:
			return 0
		else:
			if orientation == self.HORIZONTAL:
				if col == 1:
					previous_cell = self.WALL
					previous_previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row][col - 1]
					# if col > 2:
					# 	previous_previous_cell = self.current_state[row][col - 2]

				if col == 8:
					next_cell = self.WALL
				else:
					next_cell = self.current_state[row][col + 1]
					if col < 7:
						next_next_cell = self.current_state[row][col + 2]
						if col < 6:
							next_next_next_cell = self.current_state[row][col + 3]
						else:
							next_next_next_cell = self.WALL
					else:
						next_next_cell = self.WALL
			# orientation is VERTICAL
			else:
				if row == 1:
					previous_cell = self.WALL
					previous_previous_cell = self.WALL
				else:
					previous_cell = self.current_state[row - 1][col]
					# if col > 2:
					# 	previous_previous_cell = self.current_state[row][col - 2]

				if row == 8:
					next_cell = self.WALL
				else:
					next_cell = self.current_state[row + 1][col]
					if row < 7:
						next_next_cell = self.current_state[row + 2][col]
						if row < 6:
							next_next_next_cell = self.current_state[row + 3][col]
						else:
							next_next_next_cell = self.WALL
					else:
						next_next_cell = self.WALL


			if previous_cell == self.WALL and next_cell == char_to_check and next_next_cell == char_to_check and next_next_next_cell == self.EMPTY_CHAR:
				#print('1')
				return 20000 * SIGN
			# - O O O | current_cell is the 1st O after the -	
			elif previous_cell == self.EMPTY_CHAR and next_cell == char_to_check and next_next_cell == char_to_check and next_next_next_cell == self.WALL:
				#print('2')
				return 20000 * SIGN
			# X O O O - current_cell is the 1st O after X
			elif previous_cell == other_char and next_cell == char_to_check and next_next_cell == char_to_check and next_next_next_cell == self.EMPTY_CHAR:
				#print('3')
				return 20000 * SIGN
			# - O O O X current_cell is the 1st after -
			elif previous_cell == self.EMPTY_CHAR and next_cell == char_to_check and next_next_cell == char_to_check and next_next_next_cell == other_char:
				#print('4')
				return 20000 * SIGN
			# .. - O O O - ... - 10000
			elif previous_cell == self.EMPTY_CHAR and next_cell == char_to_check and next_next_cell == char_to_check and next_next_next_cell == self.EMPTY_CHAR:
				return 50000 * SIGN
			else:
				return 0

	# the computer calls this
	def make_a_move(self):
		start_time = time.time()
		elapsed_time = 0

		best = -200000
		#depth = self.MAX_DEPTH
		depth = 2
		score = ''
		m_i = 0
		m_row = 0
		m_j = 0

		alpha = -2000000
		beta = 2000000

		char_to_check = self.COMPUTER_CHAR

		for row in range(1, 9):
			for col in range(1, 9):

				# do a move on board(later to be undone) if the cell is empty
				current_cell = self.current_state[row][col]

				if current_cell == self.EMPTY_CHAR:
					# place a move in the current row and col on the board
					self.place_the_move(row, col, char_to_check)
					


					score = self.min(depth - 1, alpha, beta)

					if score >= best:
						best = score						
						m_i = chr(row + 64)
						m_row = row
						m_j = col

					# undo the move (if it was made)
					self.undo_move(row, col)

			elapsed_time = (time.time() - start_time) * 1000

			if elapsed_time >= 5000:
				break

		print('My Move is ' + str(m_i) + ' ' + str(m_j))
		self.place_the_move(m_row, m_j, char_to_check)
		
	def min(self, depth, alpha, beta):
		char_to_check = self.OPPONENT_CHAR
		best = 200000
		score = ''
		check_4_winner_value = self.check_for_winner()
		if check_4_winner_value != 0:
			return check_4_winner_value

		if depth == 0:
			evaluate = self.evaluate(char_to_check)
			return evaluate

		for row in range(1, 9):
			for col in range(1, 9):
			
				current_cell = self.current_state[row][col]

				if current_cell == self.EMPTY_CHAR:

					# place a move in the current row and col on the board
					self.place_the_move(row, col, char_to_check)
					score = self.max(depth - 1, alpha, beta)
					if score < best:
						best = score
					# if v <= alpha then return v
					if best <= alpha:
						self.undo_move(row, col)
						return best

					# alpha <-- MAX(alpha, v)
					if best <= beta:
						beta = best

					# undo the move (if it was made)
					self.undo_move(row, col)
		return best

	def max(self, depth, alpha, beta):
		char_to_check = self.COMPUTER_CHAR
		other_char = self.OPPONENT_CHAR
		best = -200000
		score = ''
		
		#check_4_winner_value = self.check_for_winner(char_to_check, new_move_row, new_move_col)
		check_4_winner_value = self.check_for_winner()
		if check_4_winner_value != 0:
			return check_4_winner_value


		if depth == 0:
			evaluate = self.evaluate(char_to_check)
			return evaluate


		for row in range(1, 9):
			for col in range(1, 9):

				current_cell = self.current_state[row][col]

				if current_cell == self.EMPTY_CHAR:

					# place a move in the current row and col on the board
					self.place_the_move(row, col, char_to_check)

					# v <-- MAX(v, MIN-VALUE(s, alpha, beta))
					#score = self.min(depth - 1, alpha, beta, row, col)
					score = self.min(depth - 1, alpha, beta)
					if score > best:
						best = score
		

					# if v >= beta, then return v 		(v = best)
					if best >= beta:
						# MIN will not select anything > beta, and MAX is trying to find a 
						#	value > best, so no point to continue
						self.undo_move(row, col)
						return best

					# alpha = MAX(alpha, v) 		(v = best)
					if best > alpha:
						alpha = best

						# undo the move (if it was made)
					self.undo_move(row, col)

		return best

	def check_for_winner(self):
		return_value = 0

		char_to_check = self.COMPUTER_CHAR
		other_char = self.OPPONENT_CHAR
		#return_value = self.horizontal_test(char_to_check, new_move_row, new_move_col)
		return_value = self.horizontal_test(char_to_check)
		if return_value == 0:
			return_value = self.horizontal_test(other_char)

			if return_value == 0:
				return_value = self.vertical_test(char_to_check)

				if return_value == 0:
					return_value = self.vertical_test(other_char)

					return return_value

				else:
					#COMPUTER WINS
					return return_value

			else:
				# OPPONENT WINS
				return return_value

		else:
			# COMPUTER WINS
			return return_value

	# if check_game_over returns 1, then the current state is not a terminal state
	# if game is not over, then evaluate
	def check_game_over(self):
		 char_to_check = self.opponent_char

		 if self.horizontal_test(char_to_check) == -50000:
		 	print('You Win')
		 elif self.vertical_test(char_to_check) == -50000:
		 	print('You Win')

		 else:
		 	char_to_check = self.computer_char

	 		if self.horizontal_test(char_to_check) == 50000:
	 			print('I Win')
	 		elif self.vertical_test(char_to_check) == 50000:
	 			print('I win')
	 		else:
	 			return 1


