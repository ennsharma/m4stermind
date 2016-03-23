from board import Board
from mastermind import MastermindAgent
from human import HumanAgent

def play_game(agent1, agent2):
	"""
	Method that handles actual gameplay by two agents.
	"""
	board = Board()
	agent1.color, agent2.color = 'r', 'b'
	winner = board.is_won()
	while not winner:
		if board.turn_player == agent1.color:
			column = agent1.select_move(board.piece_matrix)
			board.make_move(column, agent1.color)
		elif board.turn_player == agent2.color:
			column = agent2.select_move(board.piece_matrix)
			board.make_move(column, agent2.color)
		winner = board.is_won()
	board.display_board()
	return winner
