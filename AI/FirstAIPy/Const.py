class Const:
    ROWS=3
    COLS=3
    MARK_NONE = 0
    MARK_O = 1
    MARK_X = 2
    STATE_TURN_O = 1
    STATE_TURN_X = 2
    STATE_WIN_O = 3
    STATE_WIN_X = 4
    STATE_DRAW = 5

    def rowOk(row):
        if not isinstance(row,int):
            raise ValueError("row must be an integer")
        if row < 0 or row >= Const.ROWS:
            raise ValueError("row (" + str(row) + ") must be between 0 and " + str(Const.ROWS-1))

    def colOk(col):
        if not isinstance(col,int):
            raise ValueError("column must be an integer")
        if col < 0 or col >= Const.COLS:
            raise ValueError("column (" + str(col) + ") must be between 0 and " + str(Const.COLS-1))

    def markOk(mark):
        if not isinstance(mark,int):
            raise ValueError("mark must be an integer")
        if mark != Const.MARK_NONE and mark != Const.MARK_O and mark != Const.MARK_X:
            raise ValueError("mark (" + str(mark) + ") must be MARK_NONE, MARK_O or MARK_X")

    def markStr(mark):
        if mark == Const.MARK_O: return "o"
        if mark == Const.MARK_X: return "x"
        if mark == Const.MARK_NONE: return " "
        return "unkown mark (" + str(mark) + ")"

    def stateOk(state):
        if not isinstance(state,int):
            raise ValueError("state must be an integer")
        if (state != Const.STATE_TURN_O) and (state != Const.STATE_TURN_X) and \
           (state != Const.STATE_WIN_O) and (state != Const.STATE_WIN_X) and \
           (state != Const.STATE_DRAW):
            raise ValueError("state (" + str(state) + ") must be STATE_TURN_O, STATE_TURN_X, STATE_WIN_X, STATE_WIN_O or STATE_DRAW")

    def stateStr(state):
        if state == Const.STATE_TURN_O: return "o's turn"
        if state == Const.STATE_TURN_X: return "x's turn"
        if state == Const.STATE_WIN_O: return "o won"
        if state == Const.STATE_WIN_X: return "x won"
        if state == Const.STATE_DRAW: return "draw"
        return "unknown state (" + str(state) + ")"
