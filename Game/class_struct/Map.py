class Map:
	def __init__(self):
		# dungeon generator
		#fill map_dung with "blocked" tiles
		self.map_dung = []
		for y in range(game.const.MAP_DUNG_HEIGHT):
			map_dung.append([])
			for x in range(game.const.MAP_DUNG_WIDTH):
				map_dung[y].append(Tile(True))

		rooms = []
		num_rooms = 0
		for r in range(game.const.MAX_ROOMS):
			#random width and height
			w = random.randint(game.const.ROOM_MIN_SIZE, game.const.ROOM_MAX_SIZE)
			h = random.randint(game.const.ROOM_MIN_SIZE, game.const.ROOM_MAX_SIZE)
			#random position without going out of the boundaries of the map_dung
			x = random.randint(0, game.const.MAP_DUNG_WIDTH - w - 1)
			y = random.randint(0, game.const.MAP_DUNG_HEIGHT - h - 1)

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

	def is_blocked(self, x, y):
		if self.map_dung[y][x].blocked:
			return True
		for object in self.objects:
			if object.blocks and object.x == x and object.y == y:
				return True
		return False