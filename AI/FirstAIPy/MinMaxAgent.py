import random
from Const import Const
from Move import Move
from Game import Game

class MinMaxAgent:
    def __init__(self, side):
        if side != Const.MARK_O and side != Const.MARK_X:
            raise ValueError("side must be MARK_X or MARK_O")
        self.side = side

    def value(self,game, depth):
        ans = None
        #print(depth)
        state = game.getState()
        if state == Const.STATE_WIN_O:
            if self.side == Const.MARK_O: ans = 1
            else: ans = -1
        elif state == Const.STATE_WIN_X:
            if self.side == Const.MARK_X: ans = 1
            else: ans = -1
        elif state == Const.STATE_DRAW:
            ans = 0

        if ans != None: return (ans,0)

        if depth == 0:
            return(0,0)
        iside = 0
        if self.side == Const.MARK_O: iside = 1
        else: iside = -1

        iturn = 0
        if state == Const.STATE_TURN_O: iturn = 1
        else: iturn = -1

        myTurn = (iside == iturn)
        myOptions = 0

        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.value(game, (depth-1))
            move.unplay(game)
            
            myOptions = myOptions + 1 + moveOptions 
            if ans == None:
                ans = moveValue
            else:
                if myTurn:
                   ans = max(ans,moveValue)
                else:
                   ans = min(ans,moveValue)

        return (ans,myOptions)

    def move(self,game):
        depth = 4
        (maxValue,maxOptions)=self.value(game, depth)
        playable = []
        maxPlayableOption = 0
        for move in game.getMoves():
            move.play(game)
            (moveValue,moveOptions)=self.value(game, depth)
            move.unplay(game)
            if moveValue == maxValue:
                playable.append((move,moveOptions))
                maxPlayableOption = max(maxPlayableOption,moveOptions)

        bestPlayable = []
        for (move,options) in playable:
            if options == maxPlayableOption:
                bestPlayable.append(move)
        if (len(bestPlayable) - 1) > 0:
            spot=random.randint(0,len(bestPlayable)-1)
        else:
            #Choose random spot on gameboard, giving an error every now
            #   and again about 'list' not having attribute 'play' because
            #   it is returning a list sometimes and not other times
            print("gross")
            board = game.getBoard()
            for row in range(Const.ROWS):
                for col in range(Const.COLS):
                    if board[row][col] == Const.MARK_NONE:
                        bestPlayable.append([row, col])
                        spot = 0
        #print(bestPlayable[spot])
        return bestPlayable[spot]
