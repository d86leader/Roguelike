from Fighter import *
from Object import *
from Map import *

class Location:
	def __init__(self, game):
		fighter_component = Fighter(hp=30, defense=2, power=5, death_function=self.player_death)
		self.player = Object(0, 0, '@', 'player', "white", game, blocks=True, fighter=fighter_component)
		self.objects = [self.player]
		self.map = Map(game, self)

	def player_death(self, player):
		player.char = '%'
		player.color = "red"
	 
	def monster_death(self, monster):
		monster.char = '%'
		monster.color = "red"
		monster.blocks = False
		monster.fighter = None
		monster.ai = None
		monster.name = 'remains of ' + monster.name
		monster.send_to_back()

	def player_move_or_attack(self, dx, dy):
		x = self.player.x + dx
		y = self.player.y + dy

		target = None
		for obj in self.objects:
			if obj.x == x and obj.y == y:
				target = obj
				break

		if target is not None:
			target.fighter.attack(target)
		else:
			self.player.move(dx, dy)
