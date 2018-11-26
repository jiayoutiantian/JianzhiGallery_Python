import pdb
def LongestStringWithoutDuplication(str):
	curlength=0
	maxlength=0
	charhashtable = [None]*26
	for i in range(26):
		charhashtable[i]=-1
	strlength=len(str)
	for j in range(strlength):
		curstring = str[j]
		if charhashtable[ord(curstring)-ord('a')]==-1:
			charhashtable[ord(curstring)-ord('a')]=j
			curlength+=1
			if curlength>=maxlength:
				maxlength=curlength
		else:
			if (j-charhashtable[ord(curstring)-ord('a')])>curlength:
				curlength+=1
			else:
				curlength=j-charhashtable[ord(curstring)-ord('a')]
				charhashtable[ord(curstring)-ord('a')] =j
		if curlength>=maxlength:
			maxlength=curlength

		print('current character is %s' % curstring)
		print('current length is %d' % curlength)
	return maxlength

if __name__=='__main__':
	maxlength= LongestStringWithoutDuplication('arabcacfr')
	print(maxlength)
