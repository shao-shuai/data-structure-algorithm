class Data():
	def __init__(self, key):
		self.key = key

class hashtable():
	def __init__(self, size):
		self.size = size
		self.arr = [None] * self.size

	def insert(self, data):
		hashval = data.key % self.size

		while self.arr[hashval]:
			hashval += 1

		self.arr[hashval] = data.key

	def list_table(self):
		print(self.arr)


map = hashtable(19)

map.insert(Data(10))
map.insert(Data(19))
map.insert(Data(22))
map.insert(Data(38))
map.insert(Data(20))
map.insert(Data(58))
map.insert(Data(1))

map.list_table()