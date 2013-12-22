from Object import *

class Player(Object):
	def player_death(self, player):
		player.char = '%'
		player.color = "red"
