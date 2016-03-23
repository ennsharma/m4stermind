from search import BoardTree
from board import Board
import random

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
			if state.turn_player == board_tree.start_state.turn_player:
				return max_value(state, depth+1)
			else:
				return min_value(state, depth+1)

		# Max Player Recursive Function (Red)
		def max_value(state, depth):
			if board_tree.is_goal_state(state) or depth == self.depth:
				return self.evaluation_function(board_tree, state), random.randint(0, state.j)

			v = -float("inf")
			best_action = random.randint(0, state.j)
			for column, successor in board_tree.get_successors(state):
				successor_value = value(successor, depth)[0]
				if v < successor_value:
					v, best_action = successor_value, column
			return v, best_action

		# Min Player Recursive Function (Black)
		def min_value(state, depth):
			if board_tree.is_goal_state(state) or depth == self.depth:
				return self.evaluation_function(board_tree, state), random.randint(0, state.j)

			v = float("inf")
			best_action = random.randint(0, state.j)
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
		f1 = 0
		if goal_state:
			if state.turn_player == board_tree.start_state.turn_player:
				f1 = -float("inf")
			elif state.turn_player == board_tree.start_state.turn_swap[board_tree.start_state.turn_player]:
				f2 = float("inf")

		# Feature 2
		f2 = 0
		possible_wins = [[3,4,5,7,5,4,3],
						 [4,6,8,10,8,6,4],
						 [5,8,11,13,11,8,5],
						 [5,8,11,13,11,8,5],
						 [4,6,8,10,8,6,4],
						 [3,4,5,7,5,4,3]]
		for i in range(len(state.piece_matrix)):
			for j in range(len(state.piece_matrix[0])):
				if state.piece_matrix[i][j] == board_tree.start_state.turn_player:
					f2 = f2 + possible_wins[i][j]
				elif state.piece_matrix[i][j] == board_tree.start_state.turn_swap[board_tree.start_state.turn_player]:
					f2 = f2 - possible_wins[i][j]
		return f1 + f2

