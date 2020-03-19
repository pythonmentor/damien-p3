class MacGyver:
	'''
	Managing MacGyver : PV, position and moving it
	'''
	
	UP = 'z'
	RIGHT = 'd'
	DOWN = 's'
	LEFT = 'q'

	def __init__(self, decor_object):
		self.position = decor_object.enter
		self.life = 50
		
	def movement(self, input_user):
		if input_user == MacGyver.UP:
			self._up()
		elif input_user == MacGyver.RIGHT:
			self._right()
		elif input_user == MacGyver.DOWN:
			self._down()
		elif input_user == MacGyver.LEFT:
			self._left()
	
	def _up(self):
		#Getting MacGyver up
		self.position = (
			self.position[0]-1, 
			self.position[1],
		)
		
	def _right(self):
		#Getting MacGyver right
		self.position = (
			self.position[0],
			self.position[1]+1,
		)
		
	def _down(self):
		#Getting MacGyver down
		self.position = (
			self.position[0]+1,
			self.position[1],
		)
		
	def _left(self):
		#Getting MacGyver left
		self.position = (
			self.position[0],
			self.position[1]-1,
		)
		
	# def dead_mac(self):
		#Killing MacGyver
		#pass
		
	
		