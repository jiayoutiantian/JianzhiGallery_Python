def increment(number):
	if number==None:
		return False
	flag_overflow = False
	flag_takeover = True
	numberlength=len(number)
	for i in range(numberlength,-1):
		nsum = ord(number)-ord('0')
		if i==number:
			nsum+=1
		if nsum<10:
			number[i] = nsum+ord('0')



def printnumber(number):


def Print1ToMaxOfNDigits(n):
	if n<=0:
		return None
	else:
		number = [None]*n
		for i in range(n):
			number[i]='0'
		while (increment(number)==True):
			printnumber(number)

