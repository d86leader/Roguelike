import math, json, random

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_DUNG_WIDTH = 80
MAP_DUNG_HEIGHT = 45

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30
MAX_ROOM_MONSTERS = 3

KEY_UP = 38
KEY_DOWN = 40
KEY_LEFT = 37
KEY_RIGHT = 39

class Tile:
	def __init__(self, blocked, char=" "):
		self.char = char
		self.blocked = blocked
		self.explored = False
	def get_client_data(self):
		return {
			"char":self.char,
			"blocked":self.blocked,
			"explored":self.explored
		}

class Rect:
	def __init__(self, x, y, w, h):
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h
	def center(self):
		center_x = (self.x1 + self.x2) / 2
		center_y = (self.y1 + self.y2) / 2
		return (center_x, center_y)
	def intersect(self, other):
		return (self.x1 <= other.x2 and self.x2 >= other.x1 and
				self.y1 <= other.y2 and self.y2 >= other.y1)

class Object:
	def __init__(self, x, y, char, name, color, blocks=False, fighter=None, ai=None):
		self.x = x
		self.y = y
		self.char = char
		self.name = name
		self.color = color
		self.blocks = blocks
		self.fighter = fighter
		if self.fighter:  #let the fighter component know who owns it
			self.fighter.owner = self
		self.ai = ai
		if self.ai:  #let the AI component know who owns it
			self.ai.owner = self

	def move(self, dx, dy):
		if not is_blocked(self.x + dx, self.y + dy):
			self.x += dx
			self.y += dy

	def move_towards(self, target_x, target_y):
		#vector from this object to the target, and distance
		dx = target_x - self.x
		dy = target_y - self.y
		distance = math.sqrt(dx ** 2 + dy ** 2)
		dx = int(round(dx / distance))
		dy = int(round(dy / distance))
		self.move(dx, dy)

	def distance_to(self, other):
		dx = other.x - self.x
		dy = other.y - self.y
		return math.sqrt(dx ** 2 + dy ** 2)

	def send_to_back(self):
		global objects
		objects.remove(self)
		objects.insert(0, self)

	def get_client_data(self):
		return {
			"x":self.x,
			"y":self.y,
			"char":self.char,
			"color":self.color,
			"max_hp":self.fighter.max_hp,
			"hp":self.fighter.hp,
			"defense":self.fighter.defense,
			"power":self.fighter.power
		}

class Fighter:
	def __init__(self, hp, defense, power, death_function=None):
		self.max_hp = hp
		self.hp = hp
		self.defense = defense
		self.power = power
		self.death_function = death_function

	def attack(self, target):
		damage = self.power - target.fighter.defense

	def take_damage(self, damage):
		if damage > 0:
			self.hp -= damage
			if self.hp <= 0:
				function = self.death_function
				if function is not None:
					function(self.owner)

class BasicMonster:
	# test AI for mosters
	def take_turn(self):
		#if you can see it, it can see you
		monster = self.owner
		
		#move towards player if far away
		if monster.distance_to(player) >= 2:
			monster.move_towards(player.x, player.y)
		
		#close enough, attack! (if the player is still alive.)
		elif player.fighter.hp > 0:
			player.fighter.attack(player)

def is_blocked(x, y):
	if map_dung[y][x].blocked:
		return True

	for object in objects:
		if object.blocks and object.x == x and object.y == y:
			return True
 
	return False

def create_room(room):
	global map_dung
	for y in range(room.y1 + 1, room.y2):
		for x in range(room.x1 + 1, room.x2):
			map_dung[y][x].blocked = False

def create_h_tunnel(x1, x2, y):
	global map_dung
	for x in range(min(x1, x2), max(x1, x2) + 1):
		map_dung[y][x].blocked = False

def create_v_tunnel(y1, y2, x):
	global map_dung
	for y in range(min(y1, y2), max(y1, y2) + 1):
		map_dung[y][x].blocked = False

def make_map_dung():
	# dungeon generator
	global map_dung, player

	#fill map_dung with "blocked" tiles
	map_dung = []
	for y in range(MAP_DUNG_HEIGHT):
		map_dung.append([])
		for x in range(MAP_DUNG_WIDTH):
			map_dung[y].append(Tile(True))

	rooms = []
	num_rooms = 0
	for r in range(MAX_ROOMS):
		#random width and height
		w = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
		#random position without going out of the boundaries of the map_dung
		x = random.randint(0, MAP_DUNG_WIDTH - w - 1)
		y = random.randint(0, MAP_DUNG_HEIGHT - h - 1)

		new_room = Rect(x, y, w, h)

		failed = False
		for other_room in rooms:
			if new_room.intersect(other_room):
				failed = True
				break
 		
		if not failed:
			create_room(new_room)
			place_objects(new_room)
			(new_x, new_y) = new_room.center()
			
			if num_rooms == 0:
				player.x = new_x
				player.y = new_y
			else:
				(prev_x, prev_y) = rooms[num_rooms-1].center()
 			
				if random.randint(0, 1) == 1:
					create_h_tunnel(prev_x, new_x, prev_y)
					create_v_tunnel(prev_y, new_y, new_x)
				else:
					create_v_tunnel(prev_y, new_y, prev_x)
					create_h_tunnel(prev_x, new_x, new_y)
			rooms.append(new_room)
			num_rooms += 1

def place_objects(room):
	num_monsters = random.randint(0, MAX_ROOM_MONSTERS)
 
	for i in range(num_monsters):
		x = random.randint(room.x1, room.x2)
		y = random.randint(room.y1, room.y2)

		if not is_blocked(x, y):
			if random.randint(0, 100) < 80:  #80% chance of getting an orc
				#create an orc
				fighter_component = Fighter(hp=10, defense=0, power=3, death_function=monster_death)
				ai_component = BasicMonster()
 
				monster = Object(x, y, 'o', 'orc', 'green',
					blocks=True, fighter=fighter_component, ai=ai_component)
			else:
				#create a troll
				fighter_component = Fighter(hp=16, defense=1, power=4, death_function=monster_death)
				ai_component = BasicMonster()
 
				monster = Object(x, y, 'T', 'troll', 'darker_green',
					blocks=True, fighter=fighter_component, ai=ai_component)
 
			objects.append(monster)

def render_all():
	global sender_data
	sender_data_arr = {}
	sender_data_arr["map_dung"] = []
	for y in range(MAP_DUNG_HEIGHT):
		sender_data_arr["map_dung"].append([])
		for x in range(MAP_DUNG_WIDTH):
			sender_data_arr["map_dung"][y].append(map_dung[y][x].get_client_data())
	sender_data_arr["objects"] = []
	for i in range(len(objects)):
		sender_data_arr["objects"] = objects[i].get_client_data()
	sender_data = str(json.dumps(sender_data_arr))

def player_move_or_attack(dx, dy):
	x = player.x + dx
	y = player.y + dy

	target = None
	for obj in objects:
		if obj.x == x and obj.y == y:
			target = obj
			break

	if target is not None:
		target.fighter.attack(target)
	else:
		player.move(dx, dy)

def player_death(player):
	global game_state
	game_state = 'dead'
	player.char = '%'
	player.color = "red"
 
def monster_death(monster):
	monster.char = '%'
	monster.color = "red"
	monster.blocks = False
	monster.fighter = None
	monster.ai = None
	monster.name = 'remains of ' + monster.name
	monster.send_to_back()

sender_data = ""

def init():
	global player
	global objects
	fighter_component = Fighter(hp=30, defense=2, power=5, death_function=player_death)
	player = Object(0, 0, '@', 'player', "white", blocks=True, fighter=fighter_component)
	objects = [player]
	make_map_dung()

def game_loop():
	for obj in objects:
		if obj.ai:
			obj.ai.take_turn()

	render_all()

def handle_keys(d):
	if d == str(KEY_UP):
		player_move_or_attack(0, -1)
	elif d == str(KEY_DOWN):
		player_move_or_attack(0, 1)
	elif d == str(KEY_LEFT):
		player_move_or_attack(-1, 0)
	elif d == str(KEY_RIGHT):
		player_move_or_attack(1, 0)

	game_loop()
	global sender_data
	return sender_data

