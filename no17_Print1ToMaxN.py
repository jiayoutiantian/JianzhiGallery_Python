def Print1ToMaxN(number):
	digit=1
	numberOfDigit = 0
	while numberOfDigit<number:
		digit = digit*10
		numberOfDigit += 1
	for j in range(digit):
		print('current number is %d' % j)

if __name__ =='__main__':
	Print1ToMaxN(1)