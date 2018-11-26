import pdb

def NumberOf1(n):
	count=0
	while n:
		if n&1==1:
			count+=1
		n>>=1
	return count

def NumberOf1_solution2(n):
	flag=1
	count = 0

	while flag and flag<=1024:
		if n&flag!=0:
			count+=1
		flag<<=1
	return count

def NumberOf1_solution3(n):
	count = 0
	while n:
		n= (n-1)&n
		count+=1
	return count


if __name__=='__main__':
	count=NumberOf1(9)
	count_1=NumberOf1_solution2(9)
	count_2=NumberOf1_solution3(9)
	print count
	print count_1
	print count_2
