class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
		self.parent=None
	def NextNodeInBinaryTree(self,pnode):
		if pnode==None:
			return None
		pnext = None
		if pnode.right!=None:
			pnext = pnode.right
			while pnext.left!=None:
				pnext=pnext.left
			return pnext
		elif pnode.parent!=None:
			pcurrent=pnode
			pParent = pcurrent.parent
			while pcurent!=None and pcurrent==pParent.right:
				pcurent=pParent
				pParent=pParent.parent
			pnext=pParent
		return pnext

rootnode = TreeNode('a')
nodeb=TreeNode('b')
nodec=TreeNode('c')
nodee=TreeNode('e')
nodeh=TreeNode('h')
nodei=TreeNode('i')
nodef=TreeNode('f')
nodeg=TreeNode('g')
rootnode.left=nodeb
nodeb.left=noded
nodeb.right=nodee
nodee.left=nodeh
nodee.right=nodei
nodea.right=nodec
nodec.left=nodef
nodec.right=nodeg
nodeb.parent=nodea
noded.parent=nodeb
nodee.parent=nodeb
nodeh.parent=nodee
nodei.parent=nodee
nodec.parent=nodea
nodef.parent=nodec
nodeg.parent=nodec
