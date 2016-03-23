from search import BoardTree
from board import Board

class MinimaxAgent:
	"""
	Standard Minimax Agent.
	"""
	def __init__(self, depth):
		self.depth = depth

	def get_action(self, board_tree):
		"""
		This function runs depth-k minimax starting from the input
		board_tree starting state, where k is the initialized depth
		of the minimax agent.

		The value returned is an integer value corresponding to the 
		optimal column in which to place the next token for the given
		player.
		"""

		# Base Case Function
		def value(state, depth):
			if state.turn_player == 'r':
				return max_value(state, depth+1)
			else:
				return min_value(state, depth+1)

		# Max Player Recursive Function (Red)
		def max_value(state, depth):
			if board_tree.is_goal_state(state) or depth == self.depth:
				return self.evaluation_function(board_tree, state), None

			v = -float("inf")
			best_action = None
			for column, successor in board_tree.get_successors(state):
				successor_value = value(successor, depth)[0]
				if v < successor_value:
					v, best_action = successor_value, column
			return v, best_action

		# Min Player Recursive Function (Black)
		def min_value(state, depth):
			if board_tree.is_goal_state(state) or depth == self.depth:
				return self.evaluation_function(board_tree, state), None

			v = float("inf")
			best_action = None
			for column, successor in board_tree.get_successors(state):
				successor_value = value(successor, depth)[0]
				if v > successor_value:
					v, best_action = successor_value, column
			return v, best_action

		return value(board_tree.start_state, 0)[1]

	def evaluation_function(self, board_tree, state):
		"""
		This is an evaluation function for an input state. It 
		takes in a given state and returns a heuristic-based
		value corresponding to the expected utility from that 
		state.

		This value is then used to compute the minimax value
		of all parents of the input state by the MinimaxAgent.
		"""
		goal_state = board_tree.is_goal_state(state)

		# Feature 1 - Checks for a winning state.
		w1 = 1
		f1 = 0
		if goal_state:
			if goal_state == -1 and board_tree.start_state.turn_player == 'b':
				f1 = -float("inf")
			elif goal_state == 1 and board_tree.start_state.turn_player == 'r':
				f1 = float("inf")
			elif goal_state == -1 and board_tree.start_state.turn_player == 'r':
				f1 = -float("inf")
			elif goal_state == 1 and board_tree.start_state.turn_player == 'b':
				return float("inf")

		# Feature 2




		return w1*f1

