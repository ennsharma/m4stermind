from board import Board
from agents import MinimaxAgent
from search import BoardTree

SEARCH_DEPTH = 5

class MastermindAgent:
	def __init__(self, color):
		self.color = None

	def select_move(self, piece_matrix):
		"""
		Higher level method/class that encapsulates search
		and move determination (logic located in search.py
			and agents.py).
		"""
		mastermind = MinimaxAgent(SEARCH_DEPTH)
		current_board = Board(piece_matrix, self.color)
		board_tree = BoardTree(current_board)
		return mastermind.get_action(board_tree)

