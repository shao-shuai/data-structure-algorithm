from time import time

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

def height(root):
	if root is None:
		return -1

	left_height = height(root.left)
	right_height = height(root.right)

	print(left_height)
	print(right_height)

	return 1 + max(left_height, right_height)

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

def size_rur(root):
	if root is None:
		return 0

	left = size_rur(root.left)
	right = size_rur(root.right)

	return 1+ left + right

def size(root):
	if root is None:
		return 0

	stack = [ ]
	count = 0
	stack.append(root)

	while len(stack):

		node = stack.pop()
		count += 1

		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)

	return count

# Inorder traversal
def inorder(node, traversal):
	if node is None:
		return
	inorder(node.left, traversal)
	traversal.append(node.value)
	inorder(node.right, traversal)

	return traversal

print(inorder(tree, []))
