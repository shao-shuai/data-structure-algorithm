class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def append(self, data):
		node = Node(data)

		if self.head is None:
			self.head = node
			return

		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = node

	def prepend(self, data):
		node = Node(data)

		# if self.head is None:
		# 	self.head = node

		node.next = self.head
		self.head = node

	def insert_after_node(self, target, data):
		"""
		To use this function, there should be no duplicate in the list.
		"""
		node = Node(data)

		cur = self.head
		while cur:
			if cur.data == target:
				node.next = cur.next
				cur.next = node
				break
			else:
				cur = cur.next

	def insert_before_node(self, target, data):
		node = Node(data)

		cur = self.head
		while cur:
			if cur.next.data == target:
				node.next = cur.next
				cur.next = node
				break
			else:
				cur = cur.next

	def delete_node(self, key):
		cur = self.head

		if cur and cur.data == key:
			self.head = cur.next
			cur = None
			return

		while cur and cur.next.data != key:
			cur = cur.next

		temp = cur.next
		cur.next = temp.next
		temp = None
 
	def print_list(self):
		cur = self.head
		while cur:
			print(cur.data)
			cur = cur.next

	def len_iterative(self):
		cur = self.head

		count = 0

		while cur:
			count += 1
			cur = cur.next

		print(f'There are {count} nodes.')

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)



llist = LinkedList()
llist.prepend(10)
llist.prepend(33)
llist.prepend(55)
llist.prepend(32)
llist.prepend(19)
llist.prepend(22)
llist.prepend(1)
#llist.delete_node(19)
print(llist.len_recursive(llist.head))
