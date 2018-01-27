import random
from Const import Const
from Move import Move
from Game import Game

class RandomAgent:
    def __init__(self):
        pass

    def move(self,game):
        mark = None
        if game.getState() == Const.STATE_TURN_O:
            mark = Const.MARK_O
        if game.getState() == Const.STATE_TURN_X:
            mark = Const.MARK_X
        if mark == None:
            raise ValueError("game must be playable")
        board = game.getBoard()
        playable = []
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if board[row][col] == Const.MARK_NONE:
                    playable.append([row,col])
        spot=random.randint(0,len(playable)-1)
        return Move(playable[spot][0],playable[spot][1],mark)
