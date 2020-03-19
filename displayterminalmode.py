class DisplayTerminalMode:
	'''
	Displaying the game in terminal mode
	'''
	
	WALLS_TO_DISPLAY = '#' #Choosing how we want to display walls
	HALLWAYS_TO_DISPLAY = ' ' #Choosing how we want to display hallways
	
	def refresh(self, decor_object, macgyver_object, items_object, guard_object):
		self._display_decor(decor_object, macgyver_object, items_object, guard_object)
		
	def _display_decor(self, decor_object, macgyver_object, items_object, guard_object):
		for height in range(decor_object.SIZE_MAZE):
			for length in range(decor_object.SIZE_MAZE):
				
				if (height, length) == macgyver_object.position:
					self._display_mac()
				elif (height, length) in items_object.positions:
					self._display_items((height, length), items_object.positions)
				elif (height, length) == guard_object.position:
					self._display_guard()
				elif (height, length) in decor_object.walls:
					print(DisplayTerminalMode.WALLS_TO_DISPLAY, end='')
				elif (height, length) in decor_object.hallways:
					print(DisplayTerminalMode.HALLWAYS_TO_DISPLAY, end='')
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
		
	def loading_file(self, file):
		#In charge of loading file every file we want
		pass