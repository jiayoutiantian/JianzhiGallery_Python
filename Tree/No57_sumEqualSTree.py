class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
class solution:
	def sumEqualSTree(self,root,s):
		if root==None:
			return None
		if root.left==None and root.right==None:
			if s==root.val:
				return True
			else:
				return False
		stack=[]
		leftstack = sumEqualSTree(root.left,s-root.val)
		for i in leftstack:
			i.insert()
		rightstack = sumEqualSTree(root.right,s-root.val)
		