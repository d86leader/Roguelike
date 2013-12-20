import math, json, random
import socket, threading, struct, array
from hashlib import sha1
from base64 import b64encode

from Game import *
from WebSocketServer import WebSocketServer

print(type(Location))

server = WebSocketServer(Game, 20, 9999)

"""
connect  - game.init()
get data - game.handle_keys(data)
		   send(game.sender_data)
"""
