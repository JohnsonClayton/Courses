import random
from Const import Const
from Move import Move
from State import State

'''This is what I designed to have the AI work'''
#NOTE THAT THIS NO LONGER WORKS WITH THE UPDATED GAME
#THE MOST RECENT VERSION IS THE MinMaxVsRandomGamePlay and its components
class Agent:
	
	def __init__(self):
		pass
		
	def move(self, state):
		board = state.getBoard()
		mark = None
		middle = int(Const.ROWS / 2)
		playable = []
		
		if state.getState() == Const.STATE_TURN_O:
			mark = Const.MARK_O
		elif state.getState() == Const.STATE_TURN_X:
			mark = Const.MARK_X
			
		if board[middle][middle] == Const.MARK_NONE:
			print("middle = " + str(mark))
			return state.move(middle, middle, mark)
		else:
			if board[middle+1][middle+1] == Const.MARK_NONE:
				playable.append([middle+1,middle+1])
			if board[middle+1][middle-1] == Const.MARK_NONE:
				playable.append([middle+1,middle-1])
			if board[middle-1][middle-1] == Const.MARK_NONE:
				playable.append([middle-1,middle-1])
			if board[middle-1][middle+1] == Const.MARK_NONE:
				playable.append([middle-1,middle+1])
			if len(playable) == 0:
				if board[middle+1][middle] == Const.MARK_NONE:
					playable.append([middle+1,middle])
				if board[middle][middle+1] == Const.MARK_NONE:
					playable.append([middle,middle+1])
				if board[middle-1][middle] == Const.MARK_NONE:
					playable.append([middle-1,middle])
				if board[middle][middle-1] == Const.MARK_NONE:
					playable.append([middle,middle-1])
					
		if len(playable) ==  1:
			print(str(mark) + " at " + str(playable[0][0]) + str(playable[0][1]))
			return state.move(playable[0][0], playable[0][1], mark)
		elif len(playable) == 0:
			return
		else:
			randish = random.randint(0, len(playable)-1)

		if mark ==  None:
			return
			raise ValueError("state must be playable")
		print(str(mark) + " at " + str(playable[randish][0]) + str(playable[randish][1]))
		
		return state.move(playable[randish][0], playable[randish][1], mark)
