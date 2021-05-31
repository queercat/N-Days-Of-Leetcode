class Node():
	def __init__(self, value=None, left=None, right=None):
		self.value = value 

		self.left = left
		self.right = right

	def is_balanced(self):
		root = self

		height_left = root.left.tree_height()
		height_right = root.right.tree_height()

		if abs(height_right - height_left > 1):
			return False

		return True

	def tree_height(self):
		root = self

		if not root:
			return root

		height = 0
		q = [root]

		while(True):
			size = len(q)

			if size < 1:
				return height

			height += 1

			while(size > 0):
				node = q.pop(0)

				if node.left: q.append(node.left)
				if node.right: q.append(node.right)

				size -= 1

	def __str__(self):
		return self.value

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)
root.right.right.right = Node(7)
root.right.right.right.right = Node(8)

print(root.tree_height())
print(root.is_balanced())