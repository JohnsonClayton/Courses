from Const import Const
from Move import Move
from State import State
from Agent import Agent

'''Pulled directly from https://www.github.com/wmacevoy/ai-spring2018-public'''

class Game:
	def __init__(self):
		self._state = State()
		self._agentX = Agent()
		self._agentO = Agent()
		
	def turn(self):
		if self._state.getState() == Const.STATE_TURN_O:
			move=self._agentO.move(self._state)
			self._agentO.move(self._state)
		if self._state.getState() == Const.STATE_TURN_X:
			move=self._agentX.move(self._state)
			self._agentX.move(self._state)
				
	def play(self):
		while self._state.getState() == Const.STATE_TURN_O or self._state.getState() == Const.STATE_TURN_X: self.turn()
		print("game over")
		if self._state.getState() == Const.STATE_WIN_O:
			print("O won")
		elif self._state.getState() == Const.STATE_WIN_X:
			print("X won")
		elif self._state.getState() == Const.STATE_DRAW:
			print("draw")
		
if __name__ == '__main__':
	game = Game()
	game.play()
