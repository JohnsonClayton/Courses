class WaterBottle:
    def __init__(self):
        self._maxQuantity = 1000
        self._quantity = 0
        self._liquid = 'none'
	
    def getQuantity(self):
        return '{}%'.format(self._quantity * 100 /self._maxQuantity)+' or {} Liters'.format(self._quantity)
	
    def getLiquid(self):
        return self._liquid
        
    def addLiquid(self, amount, liquid):
        if self._liquid == 'none':
            self._liquid = liquid
        elif self._liquid != liquid:
            ValueError("Cannot have 2 different liquids in this container!")
        if (self._quantity + amount) > self._maxQuantity:
            ValueError("Cannot overflow the container!")
        self._quantity = self._quantity + amount
        
    def removeLiquid(self, amount):
        if self._quantity < amount:
            ValueError("Cannot remove more than what is inside the container!")
        self._quantity = self._quantity - amount
