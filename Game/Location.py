from Fighter import *
from Object import *
from MapDung import *
from Player import *

class Location:
	def __init__(self, game):
		fighter_component = Fighter(hp=30, defense=2, power=5, death_function=Player.player_death)
		self.player = Player(0, 0, '@', 'player', "white", game, blocks=True, fighter=fighter_component)
		self.objects = [self.player]
		self.map = MapDung(game, self)
