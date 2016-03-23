from board import Board

class HumanAgent:
	def __init__(self):
		self.color = None

	def select_move(self, piece_matrix):
		"""
		Higher level method/class that allows a human agent
		to play, taking input from stdin as the desired move.
		"""
		current_board = Board(piece_matrix, self.color)
		current_board.display_board()

		selected_move = input()
		try:
			return int(selected_move)
		except:
			print("Invalid move.\n")
			return self.select_move(piece_matrix)
