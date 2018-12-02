import pdb
class Listnode:
	def __init__(self,x=None):
		self.val=x
		self.next=None

class Solution:
	def printKthNode(self,pnode,k):
		if pnode==None:
			return None
		if k<=0:
			return False
		phead=pnode
		phead_slow=pnode
		for i in range(0,k):
			if phead!=None:
				phead=phead.next
			else:
				return None
		while phead!=None and phead_slow!=None:
			phead=phead.next
			phead_slow=phead_slow.next
		return phead_slow

node1=Listnode(10)
node2=Listnode(11)
node3=Listnode(12)
node1.next=node2
node2.next=node3
s=Solution()
print(s.printKthNode(node1,2).val)

