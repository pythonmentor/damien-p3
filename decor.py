class Decor:
	'''
	In charge of decor. Managing walls, hallways, enter and exit
	'''
	
	WALLS = '#' #How walls are define in maze file
	HALLWAYS = ' ' #How walls are define in maze file
	ENTER = 'E' 
	EXIT_MAZE = 'X'
	SIZE_MAZE = 15

	def __init__(self, maze_file):
		self.walls, self.hallways = self._get_walls_and_hallways(maze_file)
		self.enter, self.exit_maze = self._get_enter_and_exit(maze_file)
		
	def _get_walls_and_hallways(self, maze_file):
		#Building two sets of walls and hallways based on a maze file
		walls = set()
		hallways = set()
		height = 0
		length = 0
		
		with open(maze_file) as file:
			for line in file:
				for element in line:
					if element == Decor.WALLS:
						walls.add((height, length))
						length += 1
					elif element == Decor.HALLWAYS:
						hallways.add((height, length))
						length += 1
				length = 0
				height += 1
				
		return walls, hallways
			
		
	def _get_enter_and_exit(self, maze_file):
		#Getting enter and exit coordinates from the hallways set
		enter = tuple()
		exit_maze = tuple()
		height = 0
		length = 0
		
		with open(maze_file) as file:
			for line in file:
				for element in line:
					if element == Decor.ENTER:
						enter = (height, length)
						length += 1
					elif element == Decor.EXIT_MAZE:
						exit_maze = (height, length)
						length += 1
					else:
						length += 1
				length = 0
				height += 1
		
		return enter, exit_maze
	
	def is_hallways(self, macgyver_object):
		#Checking if coordinates are an hallway... or walls.
		if macgyver_object.position in self.hallways:
			return True