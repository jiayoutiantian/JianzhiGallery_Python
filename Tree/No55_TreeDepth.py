class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
class solution:
	def treedepth(self,root):
		if root==None:
			return None:
		if not root.left and not root.right:
			depthOfTree=1
			return depthOfTree
		LdepthOfTree = self.treedepth(root.left)
		RdepthOfTree = self.treedepth(root.right)
		depthOfTree = max(LdepthOfTree,RdepthOfTree)
		return depthOfTree

