import configuration

class DisplayTerminalMode:
	'''
	Displaying the game in terminal mode
	'''
	
	def refresh(self, 
				decor_object, 
				macgyver_object, 
				items_object, 
				guard_object,
				):
				
		self._display_decor(decor_object, 
							macgyver_object, 
							items_object, 
							guard_object,
							)
		#Display is refreshed every movement
		
	def _display_decor(self, 
						decor_object, 
						macgyver_object, 
						items_object, 
						guard_object
						):
						
		#Displaying decor
		for height in range(configuration.SIZE_MAZE):
			for length in range(configuration.SIZE_MAZE):
				
				if (height, length) == macgyver_object.position:
					#If coordinates matches MacGyver position, display him
					self._display_mac()
				elif (height, length) in items_object.positions:
					#If coordinates matches an item position, display it
					self._display_items((height, length), items_object.positions)
				elif (height, length) == guard_object.position:
					#If coordinates matches an guard position, display him
					self._display_guard()
				elif (height, length) in decor_object.walls:
					#Finally, if coordinates matches a wall, display it
					print(configuration.WALLS_TO_DISPLAY, end='')
				elif (height, length) in decor_object.hallways:
					#Or a hallway, display it
					print(configuration.HALLWAYS_TO_DISPLAY, end='')
				elif (height, length) == decor_object.enter:
					#If it's the enter of the maze, display it too.
					print(' ', end='')
			print()
		
	def _display_items(self, coordinates, items_positions):
		if items_positions[coordinates] == 'syringe':
			print('>', end='')
		elif items_positions[coordinates] == 'pipe':
			print('-', end='')
		elif items_positions[coordinates] == 'ether':
			print('o', end='')
		
	def _display_mac(self):
		print('.', end='')
		
	def _display_guard(self):
		print('x', end='')