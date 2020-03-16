class Decor:
	'''
	In charge of handling decor of the maze : walls, hallways, enter, exit
	'''
	
	SIZE = 15
	
	def __init__(self):
		self.hallways = set()
		self.enter = tuple()
		self.exit = tuple()
	
	def loading_file(self):
		#Getting coordinates of hallways, enter and exit and displaying maze with
		#class DisplayTerminal/DisplayGraphical
		pass
		
	def is_not_walls(self, coordinates):
		#Checking if (coordinates) is not a wall
		pass
		
	