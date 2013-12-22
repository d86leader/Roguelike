class Tile:
	def __init__(self, prop):
		self.char = prop["char"]
		self.blocked = prop["blocked"]
		self.explored = False
		self.color = prop["color"]
		self.color_back = prop["color_back"]

Tiles = {
	"wall" : {"blocked":True, "char":" ", "color":"white", "color_back":"black"}
}