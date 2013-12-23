class BasicMonster:
	# test AI for mosters
	def take_turn(self):
		#if you can see it, it can see you
		monster = self.owner
		
		i_min = 0
		for pl in range(len(monster.game.location.players)):
			if monster.move_towards(monster.game.location.players[pl].x, monster.game.location.players[pl].y) < monster.move_towards(monster.game.location.players[i_min].x, monster.game.location.players[i_min].y):
				i_min = pl
		player = monster.game.location.players[i_min]
		#move towards player if far away
		if monster.distance_to(player) >= 2:
			monster.move_towards(player.x, player.y)
		
		#close enough, attack! (if the player is still alive.)
		elif player.fighter.hp > 0:
			player.fighter.attack(player)