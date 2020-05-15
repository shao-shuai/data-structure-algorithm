class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST():
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(data, self.root)

	def _insert(self, data, cur_node):
		if data < cur_node.data:
			if cur_node.left is None:
				cur_node.left = Node(data)
			else:
				self._insert(data, cur_node.left)

		elif data > cur_node.data:
			if cur_node.right is None:
				cur_node.right = Node(data)
			else:
				self._insert(data, cur_node.right)

		else:
			print("Value is already in the tree.")

	def find(self, data):
		if self.root:
			is_found = self._find(data, self.root)
			if is_found:
				return True
			return False
		else:
			return None

	def _find(self, data, cur_node):
		if data > cur_node.data and cur_node.right:
			return self._find(data, cur_node.right)
		elif data < cur_node.data and cur_node.left:
			return self._find(data, cur_node.left)
		if data == cur_node.data:
			return True

	def inorder(self, node, traversal):
		if node is None:
			return
		self.inorder(node.left, traversal)
		traversal.append(node.data)
		self.inorder(node.right, traversal)
		return traversal

	def levelorder(self, node):
		queue = [ ]
		traversal = [ ]
		queue.append(node)

		while len(queue):
			# Here we need to append the value of last element in the queue, used to make mistake here.
			traversal.append(queue[-1].data)

			node = queue.pop()

			if node.left:
				queue.insert(0, node.left)
			if node.right:
				queue.insert(0, node.right)

		return traversal

	def printTree(self):
		return self.levelorder(self.root)

	



bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.inorder(bst.root, []))



