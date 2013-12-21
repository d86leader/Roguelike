class BasicMonster:
	# test AI for mosters
	def take_turn(self):
		#if you can see it, it can see you
		monster = self.owner
		
		#move towards player if far away
		if monster.distance_to(monster.game.location.player) >= 2:
			monster.move_towards(monster.game.location.player.x, monster.game.location.player.y)
		
		#close enough, attack! (if the player is still alive.)
		elif monster.game.location.player.fighter.hp > 0:
			monster.game.location.player.fighter.attack(player)