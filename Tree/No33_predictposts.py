class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
class solution:
	def predictposts(self,sequence):
		if sequence==[]:
			return False
		root=sequence[-1]
		sequenceL = list(sequence)
		length=len(squenceL)
		index=0
		for i in range(length-1):
			if sequence[i]>root:
				return index =i
				break
		for i in range(index+1,length-1):
			if sequence[i]<root:
				return False
		left=True
		if index>0:
			left=self.predictposts(sequence[:index])
		right=True
		if index<length-1:
			right=self.predictposts(sequence[index:length-1])
		return left and right