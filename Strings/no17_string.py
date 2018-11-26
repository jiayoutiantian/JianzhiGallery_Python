import pdb
def Increment(number):
	flag_overflow = False
	flag_takeover = 0
	strlennumber = len(number)
	digit_str = ['0','1','2','3','4','5','6','7','8','9']
	for i in range(strlennumber-1,-1,-1):
		nsum = ord(number[i])-ord('0')+flag_takeover
		if i==strlennumber-1:
			nsum+=1
		if nsum>=10:
			flag_takeover=1
			if i==0:
				flag_overflow=True
			else:
				nsum-=10
				number[i]=digit_str[nsum]
		else:
			number[i]=digit_str[nsum]
			return flag_overflow
			break


def printtopn(n):
	if n<=0:
		return False
	numberofdigits=n
	number=[]
	while numberofdigits:
		number.append('0')
		numberofdigits-=1
	while (Increment(number)==False):
		print(number)

if __name__=='__main__':
	printtopn(2)

