import configuration

class Guard:
	'''
	Getting coordinates of the exit for guard position
	'''
	
	def __init__(self, decor_object):
		self.position = decor_object.exit_maze
		#Assigning guard his position, exit of the maze
		
	def killing_guard(self):
		self.position = 0
	