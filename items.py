class Items:
	'''
	About items in the maze, being dropped, position and picked update
	'''
	
	ITEMS_TO_BE_PICKED = {
						'syringe', 
						'pipe', 
						'ether',
						}
	
	def __init__(self, decor_object):
		self.items_position = dropping_items(decor_object.hallways)
		self.items_picked_up = 0
		
	def dropping_items(self, hallways):
		#Choose random position in decor_objects.hallways
		#for dropping items
		pass
		
	def pick_up_items(self, item_picked_up):
		#Item picked up, changing is coordinates to 0
		pass