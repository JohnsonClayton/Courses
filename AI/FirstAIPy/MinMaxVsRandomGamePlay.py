from Const import Const
from Move import Move
from Game import Game
from GamePlay import GamePlay
from RandomAgent import RandomAgent
from MinMaxAgent import MinMaxAgent

class MinMaxVsRandomGamePlay(GamePlay):
    def createGame(self): return Game()
    def createAgentO(self): return RandomAgent()
    def createAgentX(self): return MinMaxAgent(Const.MARK_X)

if __name__ == '__main__':
    gameplay = MinMaxVsRandomGamePlay()
    gameplay.play()
