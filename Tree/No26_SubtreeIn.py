class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
		self.parent=None
class Solution:
	def hasSubtree(self,pnode1,pnode2):
		result=False
		if pnode1!=None and pnode2!=None:
			if pnode1.val==pnode2.val:
				result = DoeshaveTree2(pnode1,pnode2)
				if not result:
					if pnode1.left!=None:
						result=hasSubtree(pnode1.left,pnode2)
					if pnode1.right!=None:
						result=hasSubtree(pnode1.right,pnode2)

	def DoesHaveTree2(self,pnode1,pnode2):
		if pnode1==None or pnode2==None:
			return None
		flag_equal= False
		if pnode1.val==pnode2.val:
			return DoeshaveTree2(pnode1.left,pnode2.left) and DoeshaveTree2(pnode1.right,pnode2.right)
		else:
			return False

