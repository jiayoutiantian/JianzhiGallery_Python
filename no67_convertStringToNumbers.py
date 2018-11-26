import pdb
def belongToNumbers(charstr):
	if ord(charstr)-ord('0')>=0 and ord(charstr)-ord('0')<=9:
		return True
	else:
		return False



def string2number(str):
	k_validinput = True
	if str==None:
		k_validinput = False
		return -1
	else:
		for i in range(len(string)):
			if i==0 and not belongToNumbers(string[i]):
				if str[i]=="+":
					flag_minus=-1
					number=0
				elif str[i]=='-':
					flag_minus=1
					number=0
				else:
					k_validinput=Frue
					break
			elif i==0 and belongToNumbers(str[i]):
				temp=str[i]
				number=int(temp)
				flag_minus=-1
			else:
				if not belongToNumbers(str[i]):
					k_validinput=False
					break
				else:
					number = number*10+int(str[i])
					if (flag_minus==1 and number<0x80000000) or (flag_minus==-1 and number>0x7FFFFFFF):
						print('the number is too large, exceeding the data size limit')
	if k_validinput==True:
		return (-1)*(flag_minus)*number
	else:
		return 0



if __name__=='__main__':
	string = '45'
#	pdb.set_trace()
	convertednumber = string2number(string)
	print(convertednumber)