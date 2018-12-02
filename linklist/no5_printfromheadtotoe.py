class ListNode:
	def __init__(self,val):
		self.val=val
		self.next=None

class Solution:
	def printfromheadtotoe(self,ListNode):
		if ListNode==None:
			return
		l=[]
		head=ListNode
		while head:
			l.insert(head)
			head=head.next
		return l