class Tile:
	def __init__(self, blocked, char=" "):
		self.char = char
		self.blocked = blocked
		self.explored = False