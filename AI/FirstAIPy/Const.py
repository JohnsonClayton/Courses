class Const:
	'''This code was pulled directly from https://www.github.com/wmacevoy/ai-spring2018-public'''
	ROWS=3
	COLS=3
	MARK_NONE=0
	MARK_O=1
	MARK_X=2
	STATE_TURN_O=1
	STATE_TURN_X=2
	STATE_WIN_O=3
	STATE_WIN_X=4
	STATE_DRAW=5
	
	def rowOk(row):
		'''Checks to make sure the input row exists on the board'''
		if not isinstance(row, int):
			raise ValueError("row must be an integer")
		if row < 0 or row >= Const.ROWS:
			raise ValueError("row (" + str(row) + ") must be between 0 and " + str(Const.ROWS-1))
	
	def colOk(col):
		'''Checks to make sure the input col exists on the board'''
		if not isinstance(col, int):
			raise ValueError("col must be an integer")
		if col < 0 or col >= Const.COLS:
			raise ValueError("row (" + str(col) + ") must be between 0 and " + str(Const.COLS-1))
	
	def markOk(mark):
		'''Confirms the validity of the mark'''
		if not isinstance(mark, int):
			raise ValueError("mark must be an integer")
		if mark != Const.MARK_NONE and mark != Const.MARK_O and mark != Const.MARK_X:
			raise ValueError("mark (" + str(mark) + ") must be MARK_NONE, MARK_O, OR MARK_X")
	
	def stateOk(state):
		'''Checks the current state of the game to make sure it isn't off task'''
		if not isinstance(state, int):
			raise ValueError("state must be an integer")
		if (state != Const.STATE_TURN_O) and (state != Const.STATE_TURN_X) and (state != Const.STATE_WIN_O) and (state != Const.STATE_WIN_X) and (state != Const.STATE_DRAW):
			raise ValueError("state (" + str(state) + ") must be STATE_TURN_O, STATE_TURN_X, STATE_WIN_O, STATE_WIN_X, OR STATE_DRAW")
