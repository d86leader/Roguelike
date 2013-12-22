import math, json
from Location import *
from Constants import *

class Game:
	def __init__(self):
		self.sender_data = ""
		self.const = Constants()
		self.location = Location(self)

	def handle_keys(self, d):
		if d == str(self.const.KEY_UP):
			self.player_move_or_attack(0, -1)
		elif d == str(self.const.KEY_DOWN):
			self.player_move_or_attack(0, 1)
		elif d == str(self.const.KEY_LEFT):
			self.player_move_or_attack(-1, 0)
		elif d == str(self.const.KEY_RIGHT):
			self.player_move_or_attack(1, 0)

		self.game_loop()
		return self.sender_data

	def game_loop(self):
		for obj in self.location.objects:
			if obj.ai:
				obj.ai.take_turn()
		self.render_all()

	def render_all(self):
		sender_data_arr = {}
		sender_data_arr["map_dung"] = self.location.map.get_client_data()
		sender_data_arr["objects"] = []
		for i in range(len(self.location.objects)):
			sender_data_arr["objects"] = self.location.objects[i].get_client_data()
		self.sender_data = str(json.dumps(sender_data_arr))

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
		x = self.location.player.x + dx
		y = self.location.player.y + dy

		target = None
		for obj in self.location.objects:
			if obj.x == x and obj.y == y:
				target = obj
				break

		if target is not None:
			target.fighter.attack(target)
		else:
			self.location.player.move(dx, dy)
