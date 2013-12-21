from Game import Game
from WebSocketServer import WebSocketServer

server = WebSocketServer(Game, 20, 9999)

"""
connect  - game.init()
get data - game.handle_keys(data)
		   send(game.sender_data)
"""
