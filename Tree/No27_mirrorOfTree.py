class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
class Solution:
	def Mirror(self,root):
		if root==None:
			return None
		if root.left==None and root.right==None:
			return root
		temp=root.left
		root.left=root.right
		root.right=temp
		self.Mirror(root.left)
		self.Mirror(root.right)

