import math, random
from Object import *
from BasicMonster import *
from Tile import *
from Rect import *
from Fighter import *

class Map:
	def __init__(self, game, location):
		# dungeon generator
		self.game = game
		self.location = location
		#fill map_dung with "blocked" tiles
		self.map_dung = []
		for y in range(self.game.const.MAP_DUNG_HEIGHT):
			self.map_dung.append([])
			for x in range(self.game.const.MAP_DUNG_WIDTH):
				self.map_dung[y].append(Tile(Tiles["wall"]))

		rooms = []
		num_rooms = 0
		for r in range(self.game.const.MAX_ROOMS):
			#random width and height
			w = random.randint(self.game.const.ROOM_MIN_SIZE, self.game.const.ROOM_MAX_SIZE)
			h = random.randint(self.game.const.ROOM_MIN_SIZE, self.game.const.ROOM_MAX_SIZE)
			#random position without going out of the boundaries of the map_dung
			x = random.randint(0, self.game.const.MAP_DUNG_WIDTH - w - 1)
			y = random.randint(0, self.game.const.MAP_DUNG_HEIGHT - h - 1)

			new_room = Rect(x, y, w, h)

			failed = False
			for other_room in rooms:
				if new_room.intersect(other_room):
					failed = True
					break
	 		
			if not failed:
				self.create_room(new_room)
				self.place_objects(new_room)
				(new_x, new_y) = new_room.center()
				
				if num_rooms == 0:
					self.location.player.x = new_x
					self.location.player.y = new_y
				else:
					(prev_x, prev_y) = rooms[num_rooms-1].center()
	 			
					if random.randint(0, 1) == 1:
						self.create_h_tunnel(prev_x, new_x, prev_y)
						self.create_v_tunnel(prev_y, new_y, new_x)
					else:
						self.create_v_tunnel(prev_y, new_y, prev_x)
						self.create_h_tunnel(prev_x, new_x, new_y)
				rooms.append(new_room)
				num_rooms += 1

	def is_blocked(self, x, y):
		if self.map_dung[y][x].blocked:
			return True
		for object in self.location.objects:
			if object.blocks and object.x == x and object.y == y:
				return True
		return False

	def create_room(self, room):
		for y in range(room.y1 + 1, room.y2):
			for x in range(room.x1 + 1, room.x2):
				self.map_dung[y][x].blocked = False

	def create_h_tunnel(self, x1, x2, y):
		for x in range(min(x1, x2), max(x1, x2) + 1):
			self.map_dung[y][x].blocked = False

	def create_v_tunnel(self, y1, y2, x):
		for y in range(min(y1, y2), max(y1, y2) + 1):
			self.map_dung[y][x].blocked = False

	def place_objects(self, room):
		num_monsters = random.randint(0, self.game.const.MAX_ROOM_MONSTERS)
		for i in range(num_monsters):
			x = random.randint(room.x1, room.x2)
			y = random.randint(room.y1, room.y2)

			if not self.is_blocked(x, y):
				if random.randint(0, 100) < 80:  #80% chance of getting an orc
					#create an orc
					fighter_component = Fighter(hp=10, defense=0, power=3, death_function=self.location.monster_death)
					ai_component = BasicMonster()
					monster = Object(x, y, 'o', 'orc', 'green', self.game, blocks=True, fighter=fighter_component, ai=ai_component)
				else:
					#create a troll
					fighter_component = Fighter(hp=16, defense=1, power=4, death_function=self.location.monster_death)
					ai_component = BasicMonster()
					monster = Object(x, y, 'T', 'troll', 'darker_green', self.game, blocks=True, fighter=fighter_component, ai=ai_component)
	
				self.location.objects.append(monster)

	def get_client_data(self):
		map_json = self.map_dung
		for y in range(self.game.const.MAP_DUNG_HEIGHT):
			for x in range(self.game.const.MAP_DUNG_WIDTH):
				if self.map_dung[y][x].explored:
					map_json[y][x] = {
						"char": self.map_dung[y][x].char,
						"color": self.map_dung[y][x].color,
						"color_back": self.map_dung[y][x].color_back
					}
				else:
					map_json[y][x] = {
						"char": " ",
						"color": "white",
						"color_back": "black"
					}
		return map_json