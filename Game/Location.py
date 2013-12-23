from Fighter import *
from Object import *
from MapDung import *
from Player import *

class Location:
	def __init__(self, game, players):
		self.objects = []
		self.players = players
		self.map = MapDung(game, self)
