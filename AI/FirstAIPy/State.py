from Const import Const
from Move import Move

'''Pulled directly from https://www.github.com/wmacevoy/ai-spring2018-public'''

class State:
	def __init__(self):
		self.reset()
	def moveOk(self, row, col, mark):
		Const.rowOk(row)
		Const.colOk(col)
		Const.markOk(mark)
		if (self._state == Const.STATE_TURN_O) and (mark == Const.MARK_O) and self._board[row][col] == Const.MARK_NONE:
			return
		if (self._state == Const.STATE_TURN_X) and (mark == Const.MARK_X) and self._board[row][col] == Const.MARK_NONE:
			return
		raise ValueError("move invalid in current state")
		
	def _repeats(self, row, col, rowDir, colDir):
		mark = self._board[row][col]
		count = 0
		while(row >= 0 and row < Const.ROWS and col >= 0) and col < Const.COLS and self._board[row][col] == mark:
			row = row+rowDir
			col = col  + colDir
			count = count + 1
		return count
		
	def _length(self, row, col, rowDir, colDir):
		return self._repeats(row, col, rowDir, colDir)+self._repeats(row, col, -rowDir, -colDir)-1
			
	def _winRow(self, row, col):
		return self._length(row, col, 1, 0) >= 3	
	def _winCol(self, row, col):
		return self._length(row, col, 0, 1) >= 3
	def _winMainDiag(self, row, col):
		return self._length(row, col, 1, 1) >= 3
	def _winOffDiag(self, row, col):
		return self._length(row, col, 1, -1) >= 3
		
	def _win(self, row, col):
		return self._winRow(row, col) or self._winCol(row, col) or self._winMainDiag(row, col) or self._winOffDiag(row, col)
	
	def _draw(self):
		print(str(self._unplayed))
		return self._unplayed == 0
	
	def move(self, row, col, mark):
		self.moveOk(row, col, mark)
		self._board[row][col] = mark
		self._unplayed = self._unplayed - 1
		if self._win(row, col):
			if mark == Const.MARK_O:
				self._state = Const.STATE_WIN_O
				print("State changed to O won")
			if mark == Const.MARK_X:
				self._state = Const.STATE_WIN_X
				print("State changed to X won")
		elif self._draw():
			self._state = Const.STATE_DRAW
			print("State changed to DRAW")
		else:
			if mark == Const.MARK_O:
				self._state = Const.STATE_TURN_X
			if mark == Const.MARK_X:
				self._state = Const.STATE_TURN_O
		
	def unmove(self, row, col):
		State.rowOk(row)
		State.colOk(col)
		if self._board[row][col] == Const.MARK_X:
			self._unplayed = self._unplayed + 1
			self._board[row][col] = Const.MARK_NONE
			self._state = Const.STATE_TURN_X
		if self._board[row][col] == Const.MARK_O:
			self._unplayed = self._unplayed + 1
			self._board[row][col] = Const.MARK_NONE
			self._state = Const.STATE_TURN_O
	
	def reset(self):
		self._board = [[Const.MARK_NONE for col in range(Const.COLS)] for row in range(Const.ROWS)]
		
		self._state = Const.STATE_TURN_O
		self._unplayed = Const.ROWS*Const.COLS
		
	def getBoard(self):
		return [[self._board[row][col] for col in range(Const.COLS)] for row in range(Const.ROWS)]
		
	def getState(self):
		return self._state
		
	def play(self, moves):
		for move in moves.split():
			Move.parse(move).play(self)
