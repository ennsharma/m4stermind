from board import Board

class BoardTree:
	"""
	Search Tree of Board Objects.
	"""
	def __init__(self, start_state):
		self.start_state = start_state

	def get_start_state(self):
		"""
		Returns the start state with which the board was 
		initialized (the root of the search tree).
		"""
		return self.start_state

	def get_successors(self, state):
		"""
		Computes and returns all possible successor states of the
		input state.

		TODO - implement is_valid_move function to reduce overhead/make logic more correct
		"""
		successors = []
		for column in range(len(state.piece_matrix[0])):
			piece_matrix_copy = deep_copy(state.piece_matrix)
			successor = Board(piece_matrix_copy, state.turn_player)
			successor.make_move(column, state.turn_player)
			successors.append((column, successor))
		return successors

	def is_goal_state(self, state):
		"""
		Tests whether a given input state is a goal state.
		"""
		won = 0

		# Check Rows
		for i in range(len(state.piece_matrix)):
			consecutive, curr_color = 0, 'r'
			for j in range(len(state.piece_matrix[0])):
				if state.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif state.piece_matrix[i][j] == state.turn_swap[curr_color]:
					consecutive = 1
					curr_color = state.turn_swap[curr_color]
				elif state.piece_matrix[i][j] == 0:
					consecutive = 0

				if consecutive == 4:
					if curr_color == 'r':
						return 1
					if curr_color == 'b':
						return -1

		# Check Columns
		for j in range(len(state.piece_matrix[0])):
			consecutive, curr_color = 0, 'r'
			for i in range(len(state.piece_matrix)):
				if state.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif state.piece_matrix[i][j] == state.turn_swap[curr_color]:
					consecutive = 1
					curr_color = state.turn_swap[curr_color]
				elif state.piece_matrix[i][j] == 0:
					consecutive = 0

				if consecutive == 4:
					if curr_color == 'r':
						return 1
					if curr_color == 'b':
						return -1

		# Check Positive Diagonals
		for k in range(2*len(state.piece_matrix) - 1):
			consecutive, curr_color = 0, 'r'
			for i in range(len(state.piece_matrix)):
				j = k - i
				if i < 0 or i >= len(state.piece_matrix):
					continue
				if j < 0 or j >= len(state.piece_matrix[0]):
					continue
				if state.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif state.piece_matrix[i][j] == state.turn_swap[curr_color]:
					consecutive = 1
					curr_color = state.turn_swap[curr_color]
				elif state.piece_matrix[i][j] == 0:
					consecutive = 0

				if consecutive == 4:
					if curr_color == 'r':
						return 1
					if curr_color == 'b':
						return -1

		# Check Negative Diagonals
		for i in range(len(state.piece_matrix)):
			consecutive, curr_color, j = 0, 'r', 0
			while i < len(state.piece_matrix) and j < len(state.piece_matrix[0]):
				if state.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif state.piece_matrix[i][j] == state.turn_swap[curr_color]:
					consecutive = 1
					curr_color = state.turn_swap[curr_color]
				elif state.piece_matrix[i][j] == 0:
					consecutive = 0

				if consecutive == 4:
					if curr_color == 'r':
						return 1
					if curr_color == 'b':
						return -1
				i, j = i + 1, j + 1

		for i in range(len(state.piece_matrix)):
			consecutive, curr_color, j = 0, 'r', len(state.piece_matrix[0]) - 1
			while i >= 0 and j >= 0:
				if state.piece_matrix[i][j] == curr_color:
					consecutive = consecutive + 1
				elif state.piece_matrix[i][j] == state.turn_swap[curr_color]:
					consecutive = 1
					curr_color = state.turn_swap[curr_color]
				elif state.piece_matrix[i][j] == 0:
					consecutive = 0

				if consecutive == 4:
					if curr_color == 'r':
						return 1
					if curr_color == 'b':
						return -1
				i, j = i - 1, j - 1

		return 0

def deep_copy(matrix):
	"""
	Returns a deep copy of the input matrix.
	"""
	return [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]