import json

class MapTown(Map):
	def load_town(filename):
		self.map_dung = json.loads(open(filename, "r").read())