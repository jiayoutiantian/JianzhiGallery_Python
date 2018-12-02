import pdb
class ListNode:
	def __init__(self,x=None):
		self.val=x
		self.next=None


class solution:
	def ReverseLinklist(self,phead):
		if phead==None:
			return None
		if phead.next==None:
			return phead

		preversehead = None
		prevnode = None
		pnode=phead
		pdb.set_trace()
		while pnode!=None:
			pNext = pnode.next
			if pNext==None:
				preversehead = pnode

			pnode.next=prevnode
			prevnode=pnode
			pnode=pNext
		return preversehead

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = solution()
p11 = S.ReverseLinklist(node1)

print(p11.next.val)

