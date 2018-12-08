class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
class solution:
	def preoder(self,proot):
		if proot==None:
			return None
		stack=[]
		output=[]
		pnode=proot
	while pnode or len(stack)!=0:
		while pnode:
			treestack.append(pnode)
			output.append(pnode.val)
			pnode=pnode.left
			if not pnode:
				output.append(None)
		if len(stack):
			pnode = treestack.pop(0)
			output.append(pnode.val)
			pnode=pnode.right
			if pnode==None:
				output.append()
	return output