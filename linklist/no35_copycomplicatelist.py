class Randomlistnode:
	def __init__(self,x):
		self.val=x
		self.next=None
		self.random=None
class solution:
	def clone(self,phead):
		if phead==None:
			return None
		self.clonenodes(phead)
		self.clonerandomnodes(phead)
		return self.reconnectnodes(phead)
	def clonenodes(self,phead):
		if phead==None:
			return None
		while phead!=None:
			pnewclonenode = Randomlistnode(phead.val)
			pnext = phead.next
			if pnext!=None:
				phead.next=pnewclonenode
				pnewclonenode.next=pnext
	def connectrandomnodes(self,phead):
		pnode=phead
		while pnode!=None:
			pcloned=pnode.next
			if pnode.random!=None:
				pcloned.random=pnode.random.next
			pnode=pcloned.next
	def reconnectnodes(self,phead):
		pnode=phead
		pclonedhead=pnode.next
		pclonenode=pclonedhead
		pnode.next=pclonenode.next
		pnode=pnode.next
		while pnode:
			pclonenode.next=pnode.next
			pclonenode=pclonenode.next
			pnode.next=pclonenode.next
			pnode=pnode.next
		return pclonehead

node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)




