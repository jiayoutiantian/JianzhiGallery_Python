import pdb
class solution:
	def permutation(self,ss):
		if not len(ss):
			return []
		if len(ss)==1:
			return list(ss)
		charlist = list(ss)
		pstr=[]
		pdb.set_trace()
		for i in range(len(charlist)):
			temp=self.permutation(charlist[:i] + charlist[i+1:])
			for j in temp:
				pstr.append(charlist[i]+j)
		return pstr

ss = 'acbd'
S = solution()
# print(S.Permutation(ss))
print(S.permutation(ss))
