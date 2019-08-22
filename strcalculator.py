import re

def add(str1):
    '''takes string removes all numbers from is and stores it in a list lst'''
    count = 0
    lst = re.findall(r'-?\d+',str1)
    neg_nums = []
    
    for x in lst:
        if int(x)>0:
            if int(x)<=1000:
                count += int(x)
        else:
            '''take all negative numbers from list and append it to list neg_nums'''
            neg_nums.append(int(x))
    if neg_nums:
        raise Exception('x should not be negative. The value of x was: {}'.format(neg_nums))
    return count
	

