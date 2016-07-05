class Solution(object):
	def build_tree(self):
		node = Node("A")
		tree = Tree(node)
		node.left = Node("B")
		node.right = Node("C")
		node = node.left
		node.left = Node("D")
		node.right = Node("E")
		node = node.right
		node.left = Node("H")
		node.right = Node("I")
		node = tree.root
		node = node.right
		node.left = Node("F")
		node.right = Node("G")
		return tree

	def inorder_traversal(self, node=None):
		q = [];
		while (node.left != None):
			q.append(node)
			node = node.left
		print node.value
		while (len(q) != 0):
			node = q.pop()
			print node.value
			if (node.right != None) :
				node = node.right
				self.inorder_traversal(node)


	def preorder_traversal(self, node=None):
		q = [];
		print node.value
		while (node.left != None):
			q.append(node)
			node = node.left
			print node.value
		while (len(q) != 0):
			node = q.pop()
			if (node.right != None) :
				node = node.right
				self.preorder_traversal(node)

	def postorder_traversal(self, node=None):
		q = [];
		while (node.left != None):
			q.append(node)
			node = node.left
		print node.value
		while (len(q) != 0):
			node = q.pop()
			node_tmp = node
			if (node.right != None) :
				node = node.right
				self.postorder_traversal(node)
			print node_tmp.value


class Node:
	def __init__(self, value):
		self.value = value
		self. left = None
		self.right = None
class Tree:
	def __init__(self, root=None):
		self.root = root

 
a = Solution()
tree = a.build_tree()
print "inorder_traversal"
a.inorder_traversal(tree.root)
print "preorder_traversal"
a.preorder_traversal(tree.root)
print "postorder_traversal"
a.postorder_traversal(tree.root)

