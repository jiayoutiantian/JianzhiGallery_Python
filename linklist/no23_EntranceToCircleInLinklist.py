import pdb
class Listnode:
	def __init__(self,x=None):
		self.val=x
		self.next=None

class Solution:
	def EntranceToCircleInLinklist(self,pnode):
		if pnode==None:
			return None
		pslow=pnode.next
		if pslow==None:
			return None
		pfast=pslow.next
		while pfast!=None and pslow!=None:
			if pfast==pslow:
				return pslow
			pslow=pslow.next
			pfast=pfast.next
			if pfast!=None:
				pfast=pfast.next
		return None

	def EntryNodeInLoop(self,phead):
		meetingnode=self.EntranceToCircleInLinklist(phead)
		nodeofloop=1
		ptr=meetingnode
		while ptr.next!=meetingnode:
			ptr=ptr.next
			nodeofloop+=1
		pfast=phead
		pslow=phead
		for i in range(nodeofloop):
			pfast=pfast.next
		while pfast!=pslow:
			pfast=pfast.next
			pslow=pslow.next
		pdb.set_trace()
		return pfast

node1=Listnode(1)
node2=Listnode(2)
node3=Listnode(3)
node4=Listnode(4)
node5=Listnode(5)
node6=Listnode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeInLoop(node1).val)