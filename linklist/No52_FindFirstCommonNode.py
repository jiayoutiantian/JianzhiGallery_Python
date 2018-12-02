import pdb
import numpy as np
class ListNode:
	def __init__(self,x=None):
		self.val=x
		self.next=None
class solution:
	def getlength(self,phead):
		if phead==None:
			return 0
		count=0
		while phead!=None:
			count+=1
			phead=phead.next
		return count
	def mergelinklist(self,phead1,phead2):
		if phead1==None and phead2!=None:
			return phead2
		if phead1!=None and phead2==None:
			return phead1	
		if phead1==None and phead2==None:
			return None
		n1=self.getlength(phead1)
		n2=self.getlength(phead2)
		fasterpace = np.abs(n1-n2)
		pmergehead = None
		if n1>n2:
			pmergehead = phead1
			for i in range(fasterpace):
				if phead1!=None:
					phead1=phead1.next
			while phead1!=None and phead2!=None and phead1!=phead2:
				phead1=phead1.next
				phead2=phead2.next
			return phead1
		else:
			pmergehead = phead2
			for i in range(fasterpace):
				if phead2!=None:
					phead2=phead2.next
			while phead1!=None and phead2!=None and phead1!=phead2:
				phead1=phead1.next
				phead2=phead2.next
			return phead2

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
node22.next=node3

s=solution()
pmerge = s.mergelinklist(node1,node21)
print(pmerge.val)