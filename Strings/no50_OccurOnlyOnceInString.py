import pdb
def OccurOnlyOnceInString(str):
	if str==None:
		return False
	charhashtable = [None]*256
	for i in range(256):
		charhashtable[i]=-1
	strlength = len(str)
	for j in range(strlength):
		if charhashtable[ord(str[j])-ord('a')]==-1:
			charhashtable[ord(str[j])-ord('a')] = j
		elif charhashtable[ord(str[j])-ord('a')]>-1:
			charhashtable[ord(str[j])-ord('a')] = -2
		else:
			charhashtable[ord(str[j])-ord('a')]=-2
	index=0
	minindex=strlength
	for j in range(256):
		if charhashtable[j]>-1:
			index=j
			if index<minindex:
				minindex=index
	return str[minindex]

if __name__=='__main__':
	minindex=OccurOnlyOnceInString('abaccdeff')
	print(minindex)