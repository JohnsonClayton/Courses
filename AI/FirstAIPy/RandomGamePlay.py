from Const import Const
from GamePlay import GamePlay
from Game import Game
from RandomAgent import RandomAgent

class RandomGamePlay(GamePlay):
    def createGame(self): return Game()
    def createAgentO(self): return RandomAgent()
    def createAgentX(self): return RandomAgent()    
        
if __name__ == '__main__':
    gameplay = RandomGamePlay()
    gameplay.play()
