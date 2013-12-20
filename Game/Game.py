class Game:
	def __init__(self):
		self.sender_data = ""
		self.location = Location()
		self.const = Constants()

	def handle_keys(self, d):
		if d == str(self.const.KEY_UP):
			self.location.player_move_or_attack(0, -1)
		elif d == str(self.const.KEY_DOWN):
			self.location.player_move_or_attack(0, 1)
		elif d == str(self.const.KEY_LEFT):
			self.location.player_move_or_attack(-1, 0)
		elif d == str(self.const.KEY_RIGHT):
			self.location.player_move_or_attack(1, 0)

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
		for i in range(len(objects)):
			sender_data_arr["objects"] = self.location.objects[i].get_client_data()
		self.sender_data = str(json.dumps(sender_data_arr))
