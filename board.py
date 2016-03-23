COL_WIDTH = 4

class Board:
	"""
	Class representation of the Connect 4 board.
	"""
	turn_swap = {'r' : 'b', 'b' : 'r'}

	def __init__(self, piece_matrix=[], turn_player='r', i=6, j=7):
		self.i, self.j = i, j
		if piece_matrix:
			self.piece_matrix = piece_matrix
		else:
			self.piece_matrix = [[0 for _ in range(self.j)] for _ in range(self.i)]
		self.turn_player = turn_player

	def make_move(self, column, player):
		"""
		Method that places a piece corresponding to the given
		player in the given column of the board. 

		Outputs error messages if invalid player tries to make 
		a move, the selected column is full, or the selected 
		column is out of range.
		"""
		if player != self.turn_player:
			return "It Is Not Your Turn."
		if column <= self.i or column >= 0:
			for i in range(len(self.piece_matrix)):
				if self.piece_matrix[i][column] != 0:
					if i == 0:
						return "Column Is Full. No More Pieces Can Be Added."
					self.turn_player = self.turn_swap[player]
					self.place_piece(i-1, column, player)
					return
			self.turn_player = self.turn_swap[player]
			self.place_piece(i, column, player)
			return
		return "Column # Not In Range."

	def is_valid_move(self, column, player):
		"""
		Determines whether a given move is valid.
		"""
		if player != self.turn_player:
			return False
		for i in range(len(self.piece_matrix)):
			if self.piece_matrix[i][column] == 0:
				return True
		return False

	def place_piece(self, i, j, player):
		"""
		Simply changes the current board object's
		piece_matrix to reflect the newly placed
		piece at coordinates (i, j).
		"""
		if player == 'b':
			self.piece_matrix[i][j] = 'b'
			return
		elif player == 'r':
			self.piece_matrix[i][j] = 'r'
			return
		else:
			return "Not A Valid Color."

	def display_board(self):
		"""
		Prints the board in an orderly format to stdout.
		"""
		for i in range(len(self.piece_matrix)):
			print(' '.join(str(val).ljust(COL_WIDTH) for val in self.piece_matrix[i]))

	def reset_board(self):
		"""
		Resets board, and effectively restarts the game.
		"""
		self.piece_matrix = [[0 for _ in range(self.j)] for _ in range(6)]
		self.turn_player = 'r'

	def is_won(self):
		"""
		Does thorough checking to determine whether or not the game
		has been won. Checks rows, columns, and upper/lower diagonals.

		TODO - compact into smaller package method
		"""
		won = False

		# Check Rows
		for i in range(len(self.piece_matrix)):
			consecutive, curr_color = 0, 'r'
			for j in range(len(self.piece_matrix[0])):
				if self.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif self.piece_matrix[i][j] == self.turn_swap[curr_color]:
					consecutive = 1
					curr_color = self.turn_swap[curr_color]
				elif self.piece_matrix[i][j] == 0:
					consecutive = 0
				else:
					return "Invalid Square. Error."

				if consecutive == 4:
					if curr_color == 'r':
						return "The Red Player Has Won."
					if curr_color == 'b':
						return "The Black Player Has Won."

		# Check Columns
		for j in range(len(self.piece_matrix[0])):
			consecutive, curr_color = 0, 'r'
			for i in range(len(self.piece_matrix)):
				if self.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif self.piece_matrix[i][j] == self.turn_swap[curr_color]:
					consecutive = 1
					curr_color = self.turn_swap[curr_color]
				elif self.piece_matrix[i][j] == 0:
					consecutive = 0
				else:
					return "Invalid Square. Error."

				if consecutive == 4:
					if curr_color == 'r':
						return "The Red Player Has Won."
					if curr_color == 'b':
						return "The Black Player Has Won."

		# Check Positive Diagonals
		for k in range(2*len(self.piece_matrix) - 1):
			consecutive, curr_color = 0, 'r'
			for i in range(len(self.piece_matrix)):
				j = k - i
				if i < 0 or i >= len(self.piece_matrix):
					continue
				if j < 0 or j >= len(self.piece_matrix[0]):
					continue
				if self.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif self.piece_matrix[i][j] == self.turn_swap[curr_color]:
					consecutive = 1
					curr_color = self.turn_swap[curr_color]
				elif self.piece_matrix[i][j] == 0:
					consecutive = 0
				else:
					return "Invalid Square. Error."

				if consecutive == 4:
					if curr_color == 'r':
						return "The Red Player Has Won."
					if curr_color == 'b':
						return "The Black Player Has Won."

		# Check Negative Diagonals
		for i in range(len(self.piece_matrix)):
			consecutive, curr_color, j = 0, 'r', 0
			while i < len(self.piece_matrix) and j < len(self.piece_matrix[0]):
				if self.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif self.piece_matrix[i][j] == self.turn_swap[curr_color]:
					consecutive = 1
					curr_color = self.turn_swap[curr_color]
				elif self.piece_matrix[i][j] == 0:
					consecutive = 0
				else:
					return "Invalid Square. Error."

				if consecutive == 4:
					if curr_color == 'r':
						return "The Red Player Has Won."
					if curr_color == 'b':
						return "The Black Player Has Won."
				i, j = i + 1, j + 1

		for i in range(len(self.piece_matrix)):
			consecutive, curr_color, j = 0, 'r', len(self.piece_matrix[0]) - 1
			while i >= 0 and j >= 0:
				if self.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif self.piece_matrix[i][j] == self.turn_swap[curr_color]:
					consecutive = 1
					curr_color = self.turn_swap[curr_color]
				elif self.piece_matrix[i][j] == 0:
					consecutive = 0
				else:
					return "Invalid Square. Error."

				if consecutive == 4:
					if curr_color == 'r':
						return "The Red Player Has Won."
					if curr_color == 'b':
						return "The Black Player Has Won."
				i, j = i - 1, j - 1

		return False				
