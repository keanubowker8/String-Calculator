import re

def add(str1):
	count = 0
	lst = re.findall(r'-?\d+',str1) 
	for x in lst:
		if int(x)>0:
			if int(x)<=1000:
				count += int(x)
		else:
			raise Exception('x should not exceed be negative. The value of x was: {}'.format(x))
	return count