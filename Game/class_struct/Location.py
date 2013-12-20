class Location:
	def __init__(self):
		fighter_component = Fighter(hp=30, defense=2, power=5, death_function=player_death)
		self.player = Object(0, 0, '@', 'player', "white", blocks=True, fighter=fighter_component)
		self.objects = [player]
		self.map = Map()