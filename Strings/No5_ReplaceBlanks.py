import pdb
def replaceblanks(str):
	if str==None:
		return None
	strlength = len(str)
	numberofblanks = 0
	for i in range(strlength):
		if str[i]==' ':
			numberofblanks+=1
	newlength = strlength+numberofblanks*2
	newstr = [None]*newlength
	ptr_str = strlength-1
	new_ptr_str = newlength-1
	for i in range(0,strlength):
		if str[ptr_str]!=' ':
			newstr[new_ptr_str] = str[ptr_str] 
			ptr_str-=1
			new_ptr_str-=1
		else:
			newstr[new_ptr_str]='0'
			newstr[new_ptr_str-1]='2'
			newstr[new_ptr_str-2]='%'
			ptr_str-=1
			new_ptr_str-=1
			new_ptr_str-=1
			new_ptr_str-=1
	return newstr


if __name__=="__main__":
	str = 'we are happy'
	newstr = replaceblanks(str)
	print(newstr)


		


