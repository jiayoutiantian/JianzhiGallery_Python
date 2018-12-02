import pdb
import numpy as np
class ListNode:
	def __init__(self,x=None):
		self.val=x
		self.next=None

class solution:
	def mergeranklist(self,phead1,phead2):
		if phead1==None and phead2!=None:
			return phead2
		if phead1!=None and phead2==None:
			return phead1	
		if phead1==None and phead2==None:
			return None	
		pnewhead = None
		count = 0

		if phead1.val<=phead2.val:
			pnewhead = phead1
			pnewhead.next = self.mergeranklist(phead1.next, phead2)
		else:
			pnewhead=phead2
			pnewhead.next = self.mergeranklist(phead1, phead2.next)
		return pnewhead

node1=ListNode(10)
node2=ListNode(11)
node3=ListNode(12)
node4=ListNode(14)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

node21=ListNode(1)
node22=ListNode(2)
node21.next=node22

s=solution()
pmerge = s.mergeranklist(node1,node21)
pdb.set_trace()
print(pmerge.val)


