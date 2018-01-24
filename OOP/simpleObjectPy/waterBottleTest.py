import unittest
from waterBottle import WaterBottle 

class TestWaterBottle(unittest.TestCase):
    def _testInit(self, unit):
        self.assertEqual(unit.getQuantity(), 0)
        self.assertEqual(unit.getLiquid(), 'none')
            
    def _testaddLiquid(self, unit):
        unit.addLiquid(500, 'water')
        unit.addLiquid(25, 'water')
        self.assertEqual(unit.getLiquid(), 'water')
        self.assertEqual(unit.getQuantity(), 525)
        
    def _testaddLiquidInvalid(self, unit):
        ok = False
        
        try: unit.addLiquid(self._maxQuantity + 200, 'chloride')
        except ValueError:
            ok = True
        self.assertTrue(ok)
        
        unit.addLiquid(500, 'water')
        try: unit.addLiquid(300, 'fluoride')
        except ValueError:
            ok = True
        self.assertTrue(ok)
    
    def _testRemoveLiquid(self, unit):
        unit.addLiquid(500, 'water')
        unit.removeLiquid(300)
        assertEqual(unit.getQuantity(), 200)
    def _testRemoveLiquidInvalid(self, unit):
        ok = False
        
        unit.addLiquid(500, 'water')
        try: unit.removeLiquid(600)
        except ValueError:
            ok = True
        assertTrue(ok)
        
        ok = False
        try: unit.removeLiquid(0)
        except ValueError:
            ok = True
        assertTrue(ok)
        
    def _testGetLiquid(self, unit):
        self.assertEqual(unit.getLiquid(), self._liquid)



