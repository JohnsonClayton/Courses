import math
#python test
class Point:
	def __init__(self, x=0, y=0):
		'Initializes the Point class at a given point or at 0, 0'
		self.move(x, y)
	def move(self, x, y):
		'Input the x and y coordinates of where the point will be moved to'
		self.x = x
		self.y = y
	def reset(self):
		'Resets the point to 0, 0'
		self.x = 0
		self.y = 0
	def calc_dist(self, point):
		'Calculates the distance between the point called on and the point passed into the method'
		return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
