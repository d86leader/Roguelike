from Game import Game, PlayerThread
from WebSocketServer import WebSocketServer

server = WebSocketServer(Game, PlayerThread, 20, 9999)

"""
connect  - game.init()
get data - game.handle_keys(data)
		   send(game.sender_data)
"""
