class Object:
	def __init__(self, x, y, char, name, color, blocks=False, fighter=None, ai=None):
		self.x = x
		self.y = y
		self.char = char
		self.name = name
		self.color = color
		self.blocks = blocks
		self.fighter = fighter
		if self.fighter:  #let the fighter component know who owns it
			self.fighter.owner = self
		self.ai = ai
		if self.ai:  #let the AI component know who owns it
			self.ai.owner = self

	def move(self, dx, dy):
		if not is_blocked(self.x + dx, self.y + dy):
			self.x += dx
			self.y += dy

	def move_towards(self, target_x, target_y):
		#vector from this object to the target, and distance
		dx = target_x - self.x
		dy = target_y - self.y
		distance = math.sqrt(dx ** 2 + dy ** 2)
		dx = int(round(dx / distance))
		dy = int(round(dy / distance))
		self.move(dx, dy)

	def distance_to(self, other):
		dx = other.x - self.x
		dy = other.y - self.y
		return math.sqrt(dx ** 2 + dy ** 2)

	def send_to_back(self):
		game.location.objects.remove(self)
		game.location.objects.insert(0, self)

	def get_client_data(self):
		return {
			"x":self.x,
			"y":self.y,
			"char":self.char,
			"color":self.color,
			"max_hp":self.fighter.max_hp,
			"hp":self.fighter.hp,
			"defense":self.fighter.defense,
			"power":self.fighter.power
		}