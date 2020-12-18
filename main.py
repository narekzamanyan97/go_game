from Board import *


def main():
	#print('yo')
	board = Board()


	# print(ord('A') - 64)

	print('Enter 1 You make the first move')
	print('Enter 2 Computer makes the first move')
	print('Enter 3 to quit.')

	select = input('')
	
	while select != 3:
		board = Board()
		if select == '1':
			game_over = False

			board.print_board()
			while game_over == False:

				board.get_a_move()
				board.decrement_number_of_empty_cells()
				board.print_board()

				winner = board.check_for_winner()

				if winner == -50000:
					print('You Win')
					game_over = True

				else:
					board.make_a_move()
					board.decrement_number_of_empty_cells()
					board.print_board()

					winner = board.check_for_winner()

					if winner == 50000:
						print('I Win')
						game_over == True

				if board.get_number_of_empty_cells() == 0:
					game_over = True
					print('It\'s a Draw')

		elif select == '2':
			game_over = False

			board.print_board()
			while game_over == False:
				# get_a_move returns the row and column ()
				
				board.make_a_move()
				board.decrement_number_of_empty_cells()
				board.print_board()
				winner = board.check_for_winner()

				if winner == 50000:
					print('I Win')
					game_over = True
				else:
					board.get_a_move()
					board.decrement_number_of_empty_cells()
					board.print_board()

					winner = board.check_for_winner()

					if winner == -50000:
						print('You Win')
						game_over = True

				#print('**********' + str(board.get_number_of_empty_cells()))
				if board.get_number_of_empty_cells() == 0:
					game_over = True
					print('It\'s a Draw')


		elif select == '3':
			print('Thank you')
			break

		print('Enter 1 You make the first move')
		print('Enter 2 Computer makes the first move')
		print('Enter 3 to quit.')

		select = input('')



if __name__ == "__main__":
	main()

