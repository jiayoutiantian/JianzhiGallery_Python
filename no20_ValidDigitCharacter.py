import pdb

def ValidDigitCharacter(chari):
	if ord(chari)>=ord('0') and ord(chari)<=ord('9'):
		flag= True
	else:
		flag=False
	return flag

def PredictString2Number(str):
	if str==None:
		return False
	strlength = len(str)
	flag_signed=False
	flag_int=True
	flag_point=True
	flag_exp=True
	flag_numeric=False
	for i in range(strlength):

		if str[i]=='+' or str[i]=='-':
			flag_signed = True
			begin_int = 1
		if i!=0 and flag_signed:
			flag_digit = ValidDigitCharacter(str[i])
			flag_int &= flag_digit
		else:
			if not flag_signed and str[i]!='.':
				flag_digit = ValidDigitCharacter(str[i])
				flag_int &= flag_digit

		if str[i]=='.':
			flag_numeric = flag_numeric or flag_int
			if i==0:
				flag_int=False
			elif i==1:
				if flag_signed==True:
					flag_int=False
				else:
					print('do nothing')
			else:
				flag_digit = ValidDigitCharacter(str[i])
		    	flag_float &= flag_digit

		if str[i]=='e' or str[i]=='E':
			flag_numeric = flag_numeric or flag_float
			if flag_numeric:
				flag_digit = ValidDigitCharacter(str[i])
				flag_exp &= flag_digit
			flag_numeric = flag_numeric and flag_exp
	flag_numeric = flag_int or flag_float and flag_exp
	return flag_numeric

if __name__ == '__main__':
	pdb.set_trace()
	boolval = PredictString2Number('+100')
	print(boolval)





