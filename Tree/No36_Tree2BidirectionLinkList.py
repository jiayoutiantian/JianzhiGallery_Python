class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
class solution:
	def Tree2BidirectionLinkList(self,root):
		if root==None:
			return None
		if not root.left and not root.right:
			return root
		self.Tree2BidirectionLinkList(root.left)
		left=root.left
		if left:
			while left.right!=None:
				left=left.right
			root.left=left
			left.right=root
		self.Tree2BidirectionLinkList(root.right)
		right=root.right
		if right:
			while right.left!=None:
				right=right.left
			proot.right=right
			right.left=proot
