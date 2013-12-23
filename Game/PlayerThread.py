import 

class PlayerThread(Object):
	def __init__(self, game):
		self.game = game
		fighter_component = Fighter(hp=30, defense=2, power=5, death_function=self.player_death)
		self.setAttrs(0, 0, '@', 'player', "white", game, blocks=True, fighter=fighter_component)

	def handle_keys(self, d):
		if d == str(self.game.const.KEY_UP):
			self.move_or_attack(0, -1)
		elif d == str(self.game.const.KEY_DOWN):
			self.move_or_attack(0, 1)
		elif d == str(self.game.const.KEY_LEFT):
			self.move_or_attack(-1, 0)
		elif d == str(self.game.const.KEY_RIGHT):
			self.move_or_attack(1, 0)

		self.render_all()
		return self.sender_data

	def player_move_or_attack(self, dx, dy):
		x = self.x + dx
		y = self.y + dy

		target = None
		for obj in self.location.objects:
			if obj.x == x and obj.y == y:
				target = obj
				break

		if target is not None:
			target.fighter.attack(target)
		else:
			self.move(dx, dy)

	def render_all(self):
		sender_data_arr = {}
		sender_data_arr["map_dung"] = self.game.location.map.get_client_data()
		sender_data_arr["objects"] = []
		for i in range(len(self.game.location.objects)):
			sender_data_arr["objects"] = self.game.location.objects[i].get_client_data()
		self.sender_data = str(json.dumps(sender_data_arr))

	def player_death(self, player):
		player.char = '%'
		player.color = "red"

