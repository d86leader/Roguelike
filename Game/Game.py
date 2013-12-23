import math, json, threading, time
from Location import *
from Constants import *

class Game(threading.Thread):
	def __init__(self, players):
		threading.Thread.__init__(self)
		self.sender_data = ""
		self.const = Constants()
		self.location = Location(self, players)

	def run(self):
		time.sleep()
		for obj in self.location.objects:
			if obj.ai:
				obj.ai.take_turn()
	 
	def monster_death(self, monster):
		monster.char = '%'
		monster.color = "red"
		monster.blocks = False
		monster.fighter = None
		monster.ai = None
		monster.name = 'remains of ' + monster.name
		monster.send_to_back()

