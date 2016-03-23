class Agent:
	def __init__(self):
		self.color = None

	def select_move(self, board):
		raise NotImplementedError

	def eval_function(self, board):
		raise NotImplementedError

class ConnectFourAgent(Agent):
	def __init__(self):
		raise NotImplementedError


	def select_move(self, board):
		raise NotImplementedError

	def eval_function(self, board):
		raise NotImplementedError