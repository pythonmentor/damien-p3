import configuration

class Decor:
	'''
	In charge of decor. Managing walls, hallways, enter and exit
	'''

	def __init__(self, maze_file):
		(self.walls, 
			self.hallways, 
			self.enter, 
			self.exit_maze,
		) = self._get_structure_of_maze(maze_file)
		
	def _get_structure_of_maze(self, maze_file):
		#Recovering structure of maze from the file
		walls = set()
		hallways = set()
		enter = tuple()
		exit_maze = tuple()
		
		with open(maze_file, 'r') as file:
			file = file.read().split('\n')
			
			for i in range(configuration.SIZE_MAZE):
				for j in range(configuration.SIZE_MAZE):
					if file[i][j] == configuration.WALLS:
						#Building walls in a set
						walls.add((i, j))
					elif file[i][j] == configuration.HALLWAYS:
						#Building hallways in a set
						hallways.add((i, j))
					elif file[i][j] == configuration.ENTER:
						#Creating enter
						enter = (i, j)
					elif file[i][j] == configuration.EXIT_MAZE:
						#Creating exit
						exit_maze = (i, j)
						
		return walls, hallways, enter, exit_maze
	
	def is_hallways(self, macgyver_object):
		#Checking if coordinates wanted by user
		#are an hallway... or walls.
		if macgyver_object.position in self.hallways:
			return True