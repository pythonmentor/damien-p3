class Decor:
	'''
	In charge of decor. Managing walls, hallways, enter and exit
	'''
	
	WALLS = '#' #Define what is a wall
	HALLWAYS = ' ' #Define what is a hallway

	def __init__(self, file):
		self.walls, self.hallways = self._get_walls_and_hallways(file)
		self.enter, self.exit = self._get_enter_and_exit()
		
	def _get_walls_and_hallways(self, file):
		#Building two sets of walls and hallways based on a maze file
		pass
		
	def _get_enter_and_exit(self):
		#Getting enter and exit coordinates from the hallways set
		pass
	
	def is_hallways(self, coordinates):
		#Checking if coordinates are an hallway... or walls.
		pass