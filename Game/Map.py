class Map:
	def __init__(self, game, location):
		self.game = game
		self.location = location
		self.map_dung = []

	def is_blocked(self, x, y):
		if self.map_dung[y][x].blocked:
			return True
		for object in self.location.objects:
			if object.blocks and object.x == x and object.y == y:
				return True
		return False

	def get_client_data(self):
		map_json = []
		for y in range(self.game.const.MAP_DUNG_HEIGHT):
			map_json.append([])
			for x in range(self.game.const.MAP_DUNG_WIDTH):
				if self.map_dung[y][x].explored:
					map_json[y].append({
						"char": self.map_dung[y][x].char,
						"color": self.map_dung[y][x].color,
						"color_back": self.map_dung[y][x].color_back
					})
				else:
					map_json[y].append({
						"char": " ",
						"color": "white",
						"color_back": "black"
					})
		return map_json