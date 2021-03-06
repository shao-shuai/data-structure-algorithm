class Queue():
 	def __init__(self):
 		self.items = []

 	def enqueue(self, item):
 		self.items.insert(0, item)

 	def dequeue(self):
 		if not self.is_empty():
 			return self.items.pop()

 	def is_empty(self):
 		return len(self.items) == 0

 	def peek(self):
 		if not self.is_empty():
 			return self.items[-1].value

 	def __len__(self):
 		return self.size()

 	def size(self):
 		return len(self.items)

class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop().value

	def is_empty(self):
		return len(self.items == 0)

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)


class Node():
 	def __init__(self, value):
 		self.value = value
 		self.left = None
 		self.right = None

class BinaryTree():
 	def __init__(self, root):
 		self.root = Node(root)

 	def levelorder(self, start):
 		if start is None:
 			return

 		traversal = ""
 		queue = Queue()
 		queue.enqueue(start)

 		while len(queue):
 			traversal += str(queue.peek()) + "-"
 			node = queue.dequeue()

 			if node.left:
 				queue.enqueue(node.left)
 			if node.right:
 				queue.enqueue(node.right)

 		return traversal

 	def reverseorder(self, start):
 		if start is None:
 			return

 		queue = Queue()
 		stack = Stack()
 		traversal = ""
 		queue.enqueue(start)

 		while len(queue):
 			node = queue.dequeue()

 			if node.right:
 				queue.enqueue(node.right)
 			if node.left:
 				queue.enqueue(node.left)
 			
 			stack.push(node)
 		
 		while len(stack):
 			traversal += str(stack.pop()) + "-"

 		return traversal


 	def printree(self):
 		return self.reverseorder(self.root)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.printree())
