from Const import Const
class Move:
    def __init__(self, row, col, mark):
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

    def __str__(self):
        if self._mark == None:
            mark=''
        elif self._mark == Const.MARK_X:
            mark='x'
        elif self._mark == Const.MARK_O:
            mark='o'
        else:
            mark='?'
        return mark + chr(ord('a')+self._row)+chr(ord('1')+self._col)

    def parse(str):
        mark = None
        if str[0] == 'x' or str[0] == 'X': mark = Const.MARK_X
        if str[0] == 'o' or str[0] == 'O': mark = Const.MARK_O
        if mark == None:
            i=0
        else:
            i=1
        row=ord(str[i])-ord('a')
        col=ord(str[i+1])-ord('1')
        return Move(row,col,mark)

    def play(self, game):
        mark = self._mark
        if mark == None:
            if game.getState() == Const.STATE_TURN_X:
                mark = Const.MARK_X
            if state.getState() == Const.STATE_TURN_O:
                mark = Const.MARK_O
        game.move(self._row,self._col,mark)

    def unplay(self, game):
        game.unmove(self._row,self._col)
