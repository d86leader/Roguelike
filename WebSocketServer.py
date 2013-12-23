import socket, threading, struct, time, array
from hashlib import sha1
from base64 import b64encode

class WebSocketServer:
	"""
	self.unpack_frame(d)['payload'] - unpack received data
	self.pack_frame(d, 0x1)			- pack sender data
	"""
	def __init__(self, Game, Player, max_ping_time, port):
		s = socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(('', port))
		s.listen(1)
		self.players = []
		self.game = Game(self.players, max_ping_time)
		self.game.start()
		while True:
			conn, addr = s.accept()
			self.players.append(Player(self.game, self, max_ping_time))
			self.players[-1].s = conn
			self.players[-1].start()

	def create_handshake(self, handshake):
		lines = handshake.splitlines()
		for line in lines:
			parts = line.partition(": ")
			if parts[0] == "Sec-WebSocket-Key":
				key = parts[-1]
		key += "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
		acckey = b64encode((sha1(key)).digest())
		return (
			"HTTP/1.1 101 Switching Protocols\r\n"+
			"Upgrade: websocket\r\n"+
			"Connection: Upgrade\r\n"+
			"Sec-WebSocket-Accept: %s\r\n"+
			"\r\n"
			) % (acckey)

	def unpack_frame(self, data):
		frame = {}
		byte1, byte2 = struct.unpack_from('!BB', data)
		frame['fin'] = (byte1 >> 7) & 1
		frame['opcode'] = byte1 & 0xf
		masked = (byte2 >> 7) & 1
		frame['masked'] = masked
		mask_offset = (4 if masked else 0)
		payload_hint = byte2 & 0x7f
		if payload_hint < 126:
			payload_offset = 2
			payload_length = payload_hint
		elif payload_hint == 126:
			payload_offset = 4
			payload_length = struct.unpack_from('!H',data,2)[0]
		elif payload_hint == 127:
			payload_offset = 8
			payload_length = struct.unpack_from('!Q',data,2)[0]
		frame['length'] = payload_length
		payload = array.array('B')
		payload.fromstring(data[payload_offset + mask_offset:])
		if masked:
			mask_bytes = struct.unpack_from('!BBBB',data,payload_offset)
			for i in range(len(payload)):
				payload[i] ^= mask_bytes[i % 4]
		frame['payload'] = payload.tostring()
		return frame

	def pack_frame(self, buf, opcode, base64=False):
		if base64:
			buf = b64encode(buf)

		b1 = 0x80 | (opcode & 0x0f)
		payload_len = len(buf)
		if payload_len <= 125:
			header = struct.pack('>BB', b1, payload_len)
		elif payload_len > 125 and payload_len < 65536:
			header = struct.pack('>BBH', b1, 126, payload_len)
		elif payload_len >= 65536:
			header = struct.pack('>BBQ', b1, 127, payload_len)

		return header+buf

