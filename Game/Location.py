import json
from MapDung import *
from MapTown import *

class Location:
	def __init__(self, game, players):
		self.objects = []
		self.players = players
		self.map = MapDung(game, self)
		self.map.dung_gen()

	def load_location(self, name):
		js = json.loads(open("./Content/"+name+".json", "r").read())
		for obj in js["objects"]:
			self.objects.append(obj)
		self.map = MapTown(game, self)
		self.map.load_town(js["map_dung"])
