import random

class Items:
	'''
	About items in the maze, being dropped, position and picked update
	'''
	
	ITEMS_TO_PICKED = {
						'syringe', 
						'pipe', 
						'ether',
						}
	
	def __init__(self, decor_object):
		self.positions = self._dropping_items(decor_object.hallways)
		self.items_carried = 0
		
	def _dropping_items(self, hallways):
		#Choose random position in decor_objects.hallways
		#for dropping items
		list_of_items = Items.ITEMS_TO_PICKED.copy()
		hallways_copy = hallways.copy()
		items_positions = dict()
		
		for i in Items.ITEMS_TO_PICKED:
			random_position = random.sample(hallways_copy, 1)[0]
			hallways_copy.discard(random_position)
			items_positions[random_position] = list_of_items.pop()
		
		return items_positions
			
		
	def picked_up_items(self, coordinates):
		#Item picked up, changing is coordinates to 0
		del self.positions[coordinates]
		self.items_carried += 1