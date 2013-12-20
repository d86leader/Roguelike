class BasicMonster:
	# test AI for mosters
	def take_turn(self):
		#if you can see it, it can see you
		monster = self.owner
		
		#move towards player if far away
		if monster.distance_to(player) >= 2:
			monster.move_towards(player.x, player.y)
		
		#close enough, attack! (if the player is still alive.)
		elif game.location.player.fighter.hp > 0:
			game.location.player.fighter.attack(player)