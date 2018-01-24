from Const import Const
class Move:
	'''Pulled directly from https://www.github.com/wmacevoy/ai-spring2018-public'''
	def __init___(self, row, col, mark):
		Const.rowOk(row)
		Const.colOk(col)
		if mark != None: Const.markOk(mark)
		self._row = row
		self._col = col
		self._mark = mark
		
	def getRow(self):
		return self._row
	def getCol(self):
		return self._col
	def getMark(self):
		return self._mark
		
	def parse(str):
		'''Parses the string input to get move information, syntax ex: xa1 (put an x on a1)'''
		mark = None
		if str[0] == 'x' or str[0] == 'X': mark = Const.MARK_X
		if str[0] == 'o' or str[0] == 'O': mark = Const.MARK_O
		if mark == None:
			i = 0
		else:
			i = 1
		row = ord(str[i])-ord('a')
		col = ord(str[i])-ord('1')
		return Move(row, col, mark)
	
	def play(self, state):
		
		mark = self._mark
		if mark == None:
			if state.getState() == Const.STATE_TURN_X:
				mark = Const.MARK_X
			if state.getState() == Const.STATE_TURN_O:
				mark = Const.MARK_O
		state.move(self._row, self._col, mark)
		
	def undo(self, state):
		state.unmove(self._row, self._col)
		
