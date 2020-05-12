class Node():
	def __init__(self, item):
		self.value = item
		self.left = None
		self.right = None

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

def bfs(root):
	if root is None:
		return

	queue = [ ]
	traversal = ""
	queue.append(root)

	while len(queue):
		traversal += str(queue[-1].value) + "-"
		node = queue.pop()

		if node.left:
			queue.insert(0, node.left)

		if node.right:
			queue.insert(0,node.right)

	return traversal

print(bfs(tree))