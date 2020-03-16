class Items:
	'''
	About items in the maze, being dropped, position and picked update
	'''
	
	def __init__(self, decor_object):
		self.syringe = self.dropping_items(decor_object)
		self.ether = self.dropping_items(decor_object)
		self.pipe = self.dropping_items(decor_object)
		
	def dropping_items(self, decor_object):
		#Choose random position in decor_objects.hallways
		#for dropping items
		pass