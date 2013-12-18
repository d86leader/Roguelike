import math, json

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30
MAX_ROOM_MONSTERS = 3

# global contaner - pseudo global space
class GameCont: pass

class Tile: pass
class Rect: pass
class Object: pass
class Fighter: pass
class BasicMonster: pass

def is_blocked(x, y): pass
def create_room(room): pass
def create_h_tunnel(x1, x2, y): pass
def create_v_tunnel(y1, y2, x): pass
def make_map(): pass
def place_objects(room): pass
def render_all(): pass
def player_move_or_attack(dx, dy): pass

sender_data = ""

def init():
	pass

def handle_keys(d):
	pass