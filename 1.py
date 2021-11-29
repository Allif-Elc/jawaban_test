input = 'alagcgcdodol'


def removeDuplicate(str):
	
	index = 0 
	
	for itr_1 in range (0,len(str)):
	
		for itr_2 in range (0,itr_1+1):
			if(str[itr_1] == str[itr_2]):
				break
				
		if (itr_2 == itr_1):
			str[index] = str[itr_2]
			index += 1
			
	temp = "".join(str[:index])
	return temp 
	
	
print(removeDuplicate(list(input)))