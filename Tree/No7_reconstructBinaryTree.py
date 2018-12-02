class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

class Solution:
	def ReconstructBinaryTree(self,pre,tin):
		if not pre and not tin:
			return None
		root = TreeNode(pre[0])
		if set(pre)!=set(tin):
			return None
		i = tin.index(pre[0])
		root.left = self.ReconstructBinaryTree(pre[1:i+1],tin[:i])
		root.right = self.ReconstructBinaryTree(pre[i+1:],tin[i+1:])
		return root
pre=[1,2,3,5,6,4]
tin=[5,3,6,2,4,1]
test=Solution()
newTree = test.reConstructBinaryTree(pre, tin)

