class Node():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def insert(node, data):
	if node is None:
		node = Node(data)
	else:
		insert_helper(data, node)

def insert_helper(data, node):
	if data < node.val:
		if node.left is None:
			node.left = Node(data)
		else:
			insert_helper(data, node.left)

	elif data > node.val:
		if node.right is None:
			node.right = Node(data)
		else:
			insert_helper(data, node.right)

	else:
		print("The val inserting is already in the Tree!!!")

def bfs(root):
	if root is None:
		return

	queue = [ ]
	traversal = ""
	queue.append(root)

	while len(queue):
		traversal += str(queue[-1].val) + "-"
		node = queue.pop()

		if node.left:
			queue.insert(0, node.left)

		if node.right:
			queue.insert(0,node.right)

	return traversal

tree = None

val = [8, 3, 10, 1, 6]

for i in val:
	insert(tree, i)

print(tree.val)

