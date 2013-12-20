class Fighter:
	def __init__(self, hp, defense, power, death_function=None):
		self.max_hp = hp
		self.hp = hp
		self.defense = defense
		self.power = power
		self.death_function = death_function

	def attack(self, target):
		damage = self.power - target.fighter.defense
		target.take_damage(damage)

	def take_damage(self, damage):
		if damage > 0:
			self.hp -= damage
			if self.hp <= 0:
				function = self.death_function
				if function is not None:
					function(self.owner)