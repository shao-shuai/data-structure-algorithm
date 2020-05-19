class Node():
	def __init__(self, val):
		self.val = val
		self.next = None


class Data():
	def __init__(self, key):
		self.key = key

class hashtable():
	def __init__(self, size):
		self.size = size
		self.arr = [None] * self.size

	def insert(self, data):
		hashval = data.key % self.size

		if self.arr[hashval] is None:
			self.arr[hashval] = Node(data.key)
		else:
			head = self.arr[hashval]

			while head.next:
				head = head.next

			head.next = Node(data.key)
			
		

	def list_table(self):
		return self.arr


map = hashtable(19)

map.insert(Data(10))
map.insert(Data(19))
map.insert(Data(22))
map.insert(Data(39))
map.insert(Data(20))
map.insert(Data(58))
map.insert(Data(1))

while map.arr[1]:
	print(map.arr[1].val)
	map.arr[1] = map.arr[1].next


